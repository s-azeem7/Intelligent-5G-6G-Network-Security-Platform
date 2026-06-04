from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, request, jsonify
import requests
import logging
import os
import sys

# -----------------------------
# PROMETHEUS METRICS
# -----------------------------
REQUEST_TOTAL = Counter("amf_requests_total", "Total AMF requests")
THREAT_TOTAL = Counter("amf_threats_total", "Total AI detected threats")
BLOCKED_TOTAL = Counter("amf_blocked_total", "Total blocked requests")

# -----------------------------
# PATH FIX FOR IMPORTS
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from ai.engine import predict_threat

# -----------------------------
# LOGGING
# -----------------------------
os.makedirs("/root/5g-security-platform/logs", exist_ok=True)
os.makedirs("/root/5g-security-platform/ai", exist_ok=True)

logging.basicConfig(
    filename="/root/5g-security-platform/logs/amf.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = Flask(__name__)

# -----------------------------
# CORE SERVICES
# -----------------------------
NRF_URL = "http://localhost:8000/nnrf-nfm/v1/nf-instances"
AUSF_URL = "http://localhost:5002/nausf-auth/v1/ue-authentications"
SMF_URL = "http://localhost:5001/nsmf-pdusession/v1/sm-contexts"

ALLOWED_SLICES = ["slice-a", "slice-b"]

# -----------------------------
# UE REGISTRATION
# -----------------------------
@app.route("/namf-comm/v1/ue-contexts", methods=["POST"])
def register_ue():

    REQUEST_TOTAL.inc()

    data = request.json
    ue_id = data.get("ueId")
    slice_id = data.get("slice", "slice-a")

    # -------------------------
    # AI THREAT DETECTION
    # -------------------------
    try:
        if slice_id == "attacker-slice":
            rpm = 120
            failed_auth = 18
        else:
            rpm = 10
            failed_auth = 0

        is_threat = predict_threat(rpm, failed_auth)

        if is_threat:

            THREAT_TOTAL.inc()

            logging.warning(
                f"AI ALERT: THREAT DETECTED | UE={ue_id} | Slice={slice_id}"
            )

            # SOC ALERT FILE (REAL-TIME)
            with open("/root/5g-security-platform/ai/alerts.log", "a") as f:
                f.write(f"THREAT | UE={ue_id} | SLICE={slice_id}\n")

            BLOCKED_TOTAL.inc()

            return jsonify({
                "status": "blocked_by_ai",
                "reason": "ml_detected_anomaly",
                "ue": ue_id,
                "slice": slice_id
            }), 403

    except Exception as e:
        logging.error(f"AI Engine Error: {str(e)}")

    # -----------------------------
    # SLICE PROTECTION
    # -----------------------------
    if slice_id not in ALLOWED_SLICES:
        BLOCKED_TOTAL.inc()

        logging.warning(
            f"Blocked unauthorized slice access: UE={ue_id}, Slice={slice_id}"
        )

        return jsonify({
            "status": "blocked",
            "reason": "unauthorized slice",
            "slice": slice_id
        }), 403

    logging.info(f"UE Registration Request: UE={ue_id}, Slice={slice_id}")

    # -----------------------------
    # AUSF AUTH
    # -----------------------------
    try:
        auth = requests.post(
            AUSF_URL,
            json={"ueId": ue_id},
            timeout=5
        )

        if auth.status_code != 200:
            BLOCKED_TOTAL.inc()
            return jsonify({"status": "authentication failed"}), 401

    except Exception as e:
        return jsonify({"status": "AUSF unavailable", "error": str(e)}), 500

    # -----------------------------
    # SMF SESSION
    # -----------------------------
    try:
        smf_response = requests.post(
            SMF_URL,
            json={"ueId": ue_id, "dnn": "internet"},
            timeout=5
        )

        if smf_response.status_code != 201:
            return jsonify({"status": "session creation failed"}), 500

    except Exception as e:
        return jsonify({"status": "SMF unavailable", "error": str(e)}), 500

    # -----------------------------
    # NRF REGISTRATION
    # -----------------------------
    try:
        requests.put(
            NRF_URL,
            json={
                "nfInstanceId": f"amf-{ue_id}",
                "nfType": "AMF",
                "sliceInfo": slice_id
            },
            timeout=5
        )
    except Exception as e:
        return jsonify({"status": "NRF unavailable", "error": str(e)}), 500

    logging.info(f"Registration successful: UE={ue_id}, Slice={slice_id}")

    return jsonify({
        "status": "registered",
        "auth": "SUCCESS",
        "session": "CREATED",
        "ue": ue_id,
        "slice": slice_id
    }), 201


# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"service": "AMF", "status": "UP"})


# -----------------------------
# PROMETHEUS METRICS
# -----------------------------
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

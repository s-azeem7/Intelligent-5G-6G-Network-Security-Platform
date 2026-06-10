from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, request, jsonify
import logging
import os
import ssl

# -----------------------------
# PROMETHEUS METRICS
# -----------------------------
REQUEST_TOTAL = Counter("smf_requests_total", "Total SMF requests")
SESSION_CREATED = Counter("smf_session_created_total", "PDU sessions created")

# -----------------------------
# LOGGING
# -----------------------------
os.makedirs("/root/5g-security-platform/logs", exist_ok=True)
logging.basicConfig(
    filename="/root/5g-security-platform/logs/smf.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = Flask(__name__)

@app.route("/nsmf-pdusession/v1/sm-contexts", methods=["POST"])
def create_session():
    REQUEST_TOTAL.inc()
    data = request.json
    ue_id = data.get("ueId")
    dnn = data.get("dnn", "internet")
    logging.info(f"PDU session creation for UE {ue_id}, DNN {dnn}")
    SESSION_CREATED.inc()
    return jsonify({"smContextRef": f"ctx-{ue_id}"}), 201

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"service": "SMF", "status": "UP"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('certs/smf.crt', 'certs/smf.key')
    context.load_verify_locations('certs/ca.crt')
    context.verify_mode = ssl.CERT_REQUIRED
    app.run(host='0.0.0.0', port=5003, ssl_context=context)

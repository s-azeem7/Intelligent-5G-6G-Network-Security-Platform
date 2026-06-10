from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, request, jsonify
import logging
import os
import ssl

# -----------------------------
# PROMETHEUS METRICS
# -----------------------------
REQUEST_TOTAL = Counter("ausf_requests_total", "Total AUSF requests")
AUTH_SUCCESS = Counter("ausf_auth_success_total", "Successful authentications")
AUTH_FAILURE = Counter("ausf_auth_failure_total", "Failed authentications")

# -----------------------------
# LOGGING
# -----------------------------
os.makedirs("/root/5g-security-platform/logs", exist_ok=True)
logging.basicConfig(
    filename="/root/5g-security-platform/logs/ausf.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = Flask(__name__)

@app.route("/nausf-auth/v1/ue-authentications", methods=["POST"])
def authenticate():
    REQUEST_TOTAL.inc()
    data = request.json
    ue_id = data.get("ueId")
    # Simulate authentication always success for demo
    # In real scenario, you would validate credentials
    logging.info(f"Authentication request for UE {ue_id}")
    AUTH_SUCCESS.inc()
    return jsonify({"authResult": "SUCCESS"}), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"service": "AUSF", "status": "UP"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('certs/ausf.crt', 'certs/ausf.key')
    context.load_verify_locations('certs/ca.crt')
    context.verify_mode = ssl.CERT_REQUIRED
    app.run(host='0.0.0.0', port=5002, ssl_context=context)

from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, request, jsonify
import logging
import os
import ssl

# -----------------------------
# PROMETHEUS METRICS
# -----------------------------
REQUEST_TOTAL = Counter("nrf_requests_total", "Total NRF requests")
REGISTRATION_TOTAL = Counter("nrf_registrations_total", "Total NF registrations")

# -----------------------------
# LOGGING
# -----------------------------
os.makedirs("/root/5g-security-platform/logs", exist_ok=True)
logging.basicConfig(
    filename="/root/5g-security-platform/logs/nrf.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = Flask(__name__)

# In-memory NF registry
nf_registry = {}

@app.route("/nnrf-nfm/v1/nf-instances", methods=["PUT"])
def register_nf():
    REQUEST_TOTAL.inc()
    data = request.json
    nf_id = data.get("nfInstanceId")
    nf_registry[nf_id] = data
    REGISTRATION_TOTAL.inc()
    logging.info(f"NF registered: {nf_id}, type: {data.get('nfType')}, slice: {data.get('sliceInfo')}")
    return jsonify({"status": "registered"}), 201

@app.route("/nnrf-nfm/v1/nf-instances", methods=["GET"])
def list_nf():
    REQUEST_TOTAL.inc()
    return jsonify(nf_registry), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"service": "NRF", "status": "UP"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    # mTLS configuration
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('certs/nrf.crt', 'certs/nrf.key')
    context.load_verify_locations('certs/ca.crt')
    context.verify_mode = ssl.CERT_REQUIRED
    app.run(host='0.0.0.0', port=5001, ssl_context=context)

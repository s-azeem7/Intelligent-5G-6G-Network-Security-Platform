from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)

# Logs
os.makedirs("/root/5g-security-platform/logs", exist_ok=True)

logging.basicConfig(
    filename="/root/5g-security-platform/logs/nrf.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Slice-aware registry
registry = {
    "slice-a": {},
    "slice-b": {}
}


@app.route("/nnrf-nfm/v1/nf-instances", methods=["PUT", "GET"])
def nf_instances():

    # REGISTER NF
    if request.method == "PUT":

        data = request.json

        nf_id = data.get("nfInstanceId")
        nf_type = data.get("nfType")
        slice_id = data.get("sliceInfo", "slice-a")

        if slice_id not in registry:
            registry[slice_id] = {}

        registry[slice_id][nf_id] = {
            "nfInstanceId": nf_id,
            "nfType": nf_type,
            "sliceInfo": slice_id
        }

        logging.info(f"NF registered: {nf_id} in {slice_id}")

        return jsonify({
            "status": "registered",
            "nf": nf_id,
            "slice": slice_id
        }), 201

    # LIST ALL NFs (slice grouped view)
    return jsonify(registry), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "service": "NRF",
        "status": "UP"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "service": "NRF",
        "status": "UP"
    })


if __name__ == "__main__":
    import ssl

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    # Server certificate
    context.load_cert_chain(
        certfile="certs/nrf.crt",
        keyfile="certs/nrf.key"
    )

    # CA that signs client certs
    context.load_verify_locations("certs/ca.crt")
    # THIS ENABLES mTLS (client verification)
    context.verify_mode = ssl.CERT_REQUIRED
    # Optional: stronger security
    context.check_hostname = False
    app.run(
        host="0.0.0.0",
        port=5001,
        ssl_context=context,
        debug=False,
        use_reloader=False
    )

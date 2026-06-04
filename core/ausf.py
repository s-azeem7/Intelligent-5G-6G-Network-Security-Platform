from flask import Flask, request, jsonify
import logging
import os

os.makedirs("/root/5g-security-platform/logs", exist_ok=True)

logging.basicConfig(
    filename="/root/5g-security-platform/logs/ausf.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = Flask(__name__)

@app.route("/nausf-auth/v1/ue-authentications", methods=["POST"])
def authenticate():

    data = request.json
    ue_id = data.get("ueId")

    logging.info(f"Authentication request received for UE {ue_id}")

    if not ue_id:
        logging.warning("Authentication failed: missing UE ID")
        return jsonify({"authResult": "FAILED"}), 401

    logging.info(f"Authentication successful for UE {ue_id}")

    return jsonify({
        "authResult": "SUCCESS",
        "ueId": ue_id
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=False, use_reloader=False)

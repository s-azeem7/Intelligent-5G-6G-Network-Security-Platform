from flask import Flask, request, jsonify
import logging
import os

os.makedirs("/root/5g-security-platform/logs", exist_ok=True)

logging.basicConfig(
    filename="/root/5g-security-platform/logs/smf.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = Flask(__name__)

@app.route("/nsmf-pdusession/v1/sm-contexts", methods=["POST"])
def create_session():

    data = request.json

    ue_id = data.get("ueId")
    dnn = data.get("dnn", "internet")

    logging.info(
        f"Session created for UE={ue_id}, DNN={dnn}"
    )

    return jsonify({
        "sessionStatus": "CREATED",
        "ueId": ue_id,
        "dnn": dnn,
        "sessionId": f"sess-{ue_id}"
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=False, use_reloader=False)

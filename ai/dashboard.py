from flask import Flask, render_template_string
import os

app = Flask(__name__)

LOG_FILE = "/root/5g-security-platform/logs/amf.log"

HTML = """
<h1> 5G Security AI Dashboard</h1>
<h3>AMF Live Logs</h3>
<pre>{{ logs }}</pre>
"""

@app.route("/")
def home():
    logs = ""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            logs = "".join(f.readlines()[-20:])
    return render_template_string(HTML, logs=logs)

app.run(host="0.0.0.0", port=7000)

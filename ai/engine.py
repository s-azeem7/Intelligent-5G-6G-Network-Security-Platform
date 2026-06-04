import sys
import joblib
import pandas as pd

model = joblib.load("ai/threat_model.pkl")

def analyze(line):
    # simple feature extraction from logs
    rpm = len(line)
    failed = 1 if "failed" in line.lower() else 0

    sample = pd.DataFrame({
        "requests_per_minute": [rpm],
        "failed_auth": [failed]
    })

    pred = model.predict(sample)

    if pred[0] == -1:
        print("THREAT DETECTED:", line)
    else:
        print("NORMAL:", line)

if __name__ == "__main__":
    for line in sys.stdin:
        analyze(line.strip())

from pathlib import Path

import joblib
import pandas as pd

# Load the trained model using an absolute path
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "threat_model.pkl"

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Trained model not found: {MODEL_PATH}. "
        "Run: python3 ai/train_model.py"
    )

model = joblib.load(MODEL_PATH)


def predict_threat(rpm, failed_auth):
    """
    Predict whether network activity is anomalous.

    rpm: Number of registration requests in the last 60 seconds.
    failed_auth: Number of failed authentication attempts
                 in the last 60 seconds.
    """

    # Validate input values
    rpm = int(rpm)
    failed_auth = int(failed_auth)

    if rpm < 0 or failed_auth < 0:
        raise ValueError("rpm and failed_auth cannot be negative")

    # Prepare input in the same feature format used during training
    sample = pd.DataFrame({
        "requests_per_minute": [rpm],
        "failed_auth": [failed_auth]
    })

    # Isolation Forest: -1 = anomaly, 1 = normal
    prediction = model.predict(sample)

    return prediction[0] == -1

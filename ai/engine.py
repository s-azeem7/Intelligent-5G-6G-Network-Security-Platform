import joblib
import pandas as pd

model = joblib.load("ai/threat_model.pkl")

def predict_threat(rpm, failed_auth):

    sample = pd.DataFrame({
        "requests_per_minute": [rpm],
        "failed_auth": [failed_auth]
    })

    pred = model.predict(sample)

    return pred[0] == -1

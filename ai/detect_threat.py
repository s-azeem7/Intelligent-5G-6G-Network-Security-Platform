import sys
import joblib
import pandas as pd

model = joblib.load("ai/threat_model.pkl")

rpm = int(sys.argv[1])
failed = int(sys.argv[2])

sample = pd.DataFrame({
    "requests_per_minute": [rpm],
    "failed_auth": [failed]
})

prediction = model.predict(sample)

if prediction[0] == -1:
    print("THREAT DETECTED")
else:
    print("NORMAL TRAFFIC")

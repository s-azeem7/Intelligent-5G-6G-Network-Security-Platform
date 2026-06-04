import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = pd.DataFrame({
    "requests_per_minute": [5,7,6,8,10,9,7,8,100,120,150],
    "failed_auth": [0,0,1,0,1,0,0,1,15,20,25]
})

model = IsolationForest(
    contamination=0.2,
    random_state=42
)

model.fit(data)

joblib.dump(model, "ai/threat_model.pkl")

print("AI Threat Model Created")

import joblib
import pandas as pd
import os

# now your imports will resolve
from co2_emissions_ml.preprocessing import build_preprocessor, build_target_transformer
from co2_emissions_ml.models import fit_cluster_model

df = pd.read_csv("data/New Dataset.csv", encoding="latin-1")
X = df.drop(columns=["CO2 Emissions(g/km)"])
y = df["CO2 Emissions(g/km)"]

pre = build_preprocessor(X)
tt = build_target_transformer()

# you can reduce n_trials to speed it up
bundle = fit_cluster_model(X, y, pre, tt, n_trials=20)

# Save the bundle back into your notebook’s working dir
os.makedirs("models", exist_ok=True)
joblib.dump(bundle, "models/bundle.pkl")
print("Bundle saved to models/bundle.pkl")

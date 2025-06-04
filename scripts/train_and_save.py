import joblib
import pandas as pd
from co2_emissions_ml.preprocessing import build_preprocessor, build_target_transformer
from co2_emissions_ml.models import fit_cluster_model


def main():
    df = pd.read_csv("data/New Dataset.csv", engine="python", encoding="ISO-8859-1")
    X = df.drop(columns=["CO2 Emissions(g/km)"])
    y = df["CO2 Emissions(g/km)"]

    pre = build_preprocessor(X)
    tt = build_target_transformer()
    bundle = fit_cluster_model(X, y, pre, tt)

    # Save to models/bundle.pkl
    joblib.dump(bundle, "models/bundle.pkl")
    print("Saved trained bundle to models/bundle.pkl")


if __name__ == "__main__":
    main()

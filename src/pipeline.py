import pandas as pd
from src.preprocessing import build_preprocessor, build_target_transformer
from src.models import fit_cluster_model, predict_bundle
from src.evaluation import compute_metrics


def run_pipeline(
    data_path: str,
    target_col: str = "CO2 Emissions (g/km)",
):
    # 1) Load data
    df = pd.read_csv(data_path)
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # 2) Build preprocessing objects
    pre = build_preprocessor(X)
    tt = build_target_transformer()

    # 3) Fit ensemble
    bundle = fit_cluster_model(X, y, pre, tt)

    # 4) Evaluate on train & test split
    from sklearn.model_selection import train_test_split

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    y_pred = predict_bundle(bundle, X_te)

    # 5) Metrics
    metrics = compute_metrics(y_te, y_pred)
    print("Test set performance:")
    for k, v in metrics.items():
        print(f"  {k}: {v:.4f}")

    return bundle, metrics


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Train & evaluate CO2 emissions pipeline"
    )
    parser.add_argument("--data", type=str, required=True, help="Path to CSV data")
    args = parser.parse_args()
    run_pipeline(args.data)

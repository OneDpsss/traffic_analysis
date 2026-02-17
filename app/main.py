import sys
from sklearn.model_selection import train_test_split

from app.preprocessing import load_and_prepare
from app.features import build_pipeline
from app.train import train_model
from app.evaluate import plot_balance, make_report, show_top_features


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m app.main path/to/data.csv")
        sys.exit(1)

    data_path = sys.argv[1]

    df = load_and_prepare(data_path)

    plot_balance(df)

    X = df[["position", "city", "salary", "age", "experience_years"]]
    y = df["y"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42,
    )

    preprocessor = build_pipeline()

    model, encoder = train_model(
        X_train,
        y_train,
        preprocessor,
    )

    make_report(model, encoder, X_test, y_test)

    show_top_features(model, top_n=10)


if __name__ == "__main__":
    main()

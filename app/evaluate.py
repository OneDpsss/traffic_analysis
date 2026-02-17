import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd



def plot_balance(df):
    plt.figure()
    sns.countplot(x="y", data=df)
    plt.title("Баланс классов junior/middle/senior")
    plt.show()


def make_report(model, encoder, X_test, y_test):

    y_pred = model.predict(X_test)
    y_test_enc = encoder.transform(y_test)

    report = classification_report(
        y_test_enc,
        y_pred,
        target_names=encoder.classes_,
    )

    print(report)


def show_top_features(model, top_n=10):

    clf = model.named_steps["clf"]
    preprocessor = model.named_steps["features"]

    feature_names = preprocessor.get_feature_names_out()

    coefs = clf.coef_

    importance = np.mean(np.abs(coefs), axis=0)

    importance = importance / importance.sum()

    feat_df = pd.DataFrame({
        "feature": feature_names,
        "importance": importance
    })

    feat_df = feat_df.sort_values("importance", ascending=False)

    print("\n2. Важность признаков (топ-10):")

    for _, row in feat_df.head(top_n).iterrows():
        print(f"   - {row['feature']}: {row['importance']:.3f}")



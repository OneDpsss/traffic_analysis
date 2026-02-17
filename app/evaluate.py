import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report


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

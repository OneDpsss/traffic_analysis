import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

from app.config import MODEL_PATH, VECTORIZER_PATH, ENCODER_PATH


def train_model(X, y, preprocessor):

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    model = Pipeline(
        steps=[
            ("features", preprocessor),
            ("clf", LogisticRegression(max_iter=1000)),
        ]
    )

    model.fit(X, y_encoded)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(encoder, ENCODER_PATH)

    return model, encoder

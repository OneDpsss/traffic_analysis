from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


def build_pipeline():
    numeric_features = ["salary", "age", "experience_years"]

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    text_transformer = TfidfVectorizer(max_features=2000)

    preprocessor = ColumnTransformer(
        transformers=[
            ("text_position", text_transformer, "position"),
            ("numeric", numeric_transformer, numeric_features)
        ]
    )

    return preprocessor

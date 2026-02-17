from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "resources" / "data" / "hh_resumes.csv"

MODEL_DIR = BASE_DIR / "resources" / "model"
MODEL_PATH = MODEL_DIR / "model.pkl"
VECTORIZER_PATH = MODEL_DIR / "vectorizer.pkl"
ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"

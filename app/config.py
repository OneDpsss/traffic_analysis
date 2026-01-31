from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RESOURCES_DIR = BASE_DIR / "resources"
MODEL_PATH = RESOURCES_DIR / "model.joblib"

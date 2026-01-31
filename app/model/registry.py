from pathlib import Path
import joblib


def save_model(model, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


def load_model(path: Path):
    if not path.exists():
        raise FileNotFoundError(
            f"Model not found at {path}. Train the model first."
        )
    return joblib.load(path)

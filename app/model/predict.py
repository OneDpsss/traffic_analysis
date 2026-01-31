import numpy as np

from app.config import MODEL_PATH
from app.model.registry import load_model


def predict(x: np.ndarray) -> list[float]:
    model = load_model(MODEL_PATH)
    preds = model.predict(x)
    return preds.astype(float).tolist()

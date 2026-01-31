import sys
import numpy as np
from sklearn.linear_model import Ridge

from app.config import MODEL_PATH
from app.model.registry import save_model


def train(x_path: str, y_path: str) -> None:
    x = np.load(x_path)
    y = np.load(y_path)

    model = Ridge(alpha=1.0, random_state=42)
    model.fit(x, y)

    save_model(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ValueError("Usage: python train.py x_data.npy y_data.npy")

    train(sys.argv[1], sys.argv[2])

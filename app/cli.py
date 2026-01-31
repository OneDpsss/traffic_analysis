import argparse
from pathlib import Path

import numpy as np

from app.model.predict import predict
from app.utils.io import load_npy, save_npy


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Predict salaries from HH.ru dataset"
    )
    parser.add_argument("x_path", help="Path to x_data.npy")
    parser.add_argument(
        "--out",
        help="Output .npy file path",
        default=None,
    )

    args = parser.parse_args()

    x_path = Path(args.x_path)
    out_path = (
        Path(args.out)
        if args.out
        else x_path.parent / "predictions.npy"
    )

    x = load_npy(x_path)
    salaries = np.array(predict(x), dtype=float)

    save_npy(salaries, out_path)

    print(f"Predictions saved to {out_path}")

import argparse
from pathlib import Path

from app.pipeline import build_pipeline
from app.context import PipelineContext


def main() -> None:
    parser = argparse.ArgumentParser(description="HH CSV preprocessing pipeline")
    parser.add_argument("csv_path", type=Path, help="Path to hh.csv")

    args = parser.parse_args()

    context = PipelineContext(csv_path=args.csv_path)
    pipeline = build_pipeline()
    pipeline.handle(context)

import re

from app.handlers.base import Handler
from app.context import PipelineContext


class ExtractAgeHandler(Handler):
    def process(self, context: PipelineContext) -> None:
        df = context.df

        def extract_age(value: str) -> int | None:
            match = re.search(r"(\d+)\s*года|\s*(\d+)\s*лет", value)
            return int(match.group(1) or match.group(2)) if match else None

        df["age"] = df["Пол, возраст"].astype(str).apply(extract_age)
        df.dropna(subset=["age"], inplace=True)

        context.df = df

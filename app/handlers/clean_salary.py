import re

from app.handlers.base import Handler
from app.context import PipelineContext


class CleanSalaryHandler(Handler):
    def process(self, context: PipelineContext) -> None:
        df = context.df

        df["ЗП"] = (
            df["ЗП"]
            .astype(str)
            .apply(lambda x: int(re.sub(r"[^\d]", "", x)) if x else None)
        )

        df.dropna(subset=["ЗП"], inplace=True)
        context.df = df

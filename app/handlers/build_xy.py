import numpy as np

from app.handlers.base import Handler
from app.context import PipelineContext


class BuildXYHandler(Handler):
    def process(self, context: PipelineContext) -> None:
        df = context.df

        numeric = df[["age", "gender"]].values
        x = np.hstack([numeric, context.text_features])
        y = df["ЗП"].values

        context.x = x
        context.y = y

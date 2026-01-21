import pandas as pd

from app.handlers.base import Handler
from app.context import PipelineContext


class LoadCSVHandler(Handler):
    def process(self, context: PipelineContext) -> None:
        context.df = pd.read_csv(context.csv_path)

from app.handlers.base import Handler
from app.context import PipelineContext


class EncodeGenderHandler(Handler):
    def process(self, context: PipelineContext) -> None:
        df = context.df

        df["gender"] = df["Пол, возраст"].str.contains("Мужчина").astype(int)

        context.df = df

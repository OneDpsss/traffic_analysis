from sklearn.feature_extraction.text import TfidfVectorizer

from app.handlers.base import Handler
from app.context import PipelineContext


TEXT_COLUMNS = [
    "Ищет работу на должность:",
    "Город",
    "Занятость",
    "График",
    "Опыт (двойное нажатие для полной версии)",
]


class VectorizeTextHandler(Handler):
    def process(self, context: PipelineContext) -> None:
        df = context.df

        text_data = (
            df[TEXT_COLUMNS]
            .fillna("")
            .agg(" ".join, axis=1)
            .values
        )

        vectorizer = TfidfVectorizer(max_features=300)
        text_features = vectorizer.fit_transform(text_data).toarray()

        context.df = df
        context.text_features = text_features

import numpy as np

from app.handlers.base import Handler
from app.context import PipelineContext


class SaveNpyHandler(Handler):
    def process(self, context: PipelineContext) -> None:
        base_path = context.csv_path.parent

        np.save(base_path / "x_data.npy", context.x)
        np.save(base_path / "y_data.npy", context.y)

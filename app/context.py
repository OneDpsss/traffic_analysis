from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd


@dataclass
class PipelineContext:
    csv_path: Path
    df: Optional[pd.DataFrame] = None

    x: Optional[np.ndarray] = None
    y: Optional[np.ndarray] = None

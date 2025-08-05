"""
Módulo de utilidades
"""

import pandas as pd
from pydantic import BaseModel


def pydantic_model_to_dataframe(model: BaseModel) -> pd.DataFrame:
    """
    Converte um modelo Pydantic para um DataFrame
    """
    data = model.model_dump()
    return pd.DataFrame.from_dict(data, orient="index").T

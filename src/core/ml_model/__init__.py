"""
Modulos de inferência
"""

from .inference.pre_process import HousePreProcessor
from .inference.regressor import HouseRegressor

__all__ = ["HousePreProcessor", "HouseRegressor"]

"""
Módulo de lógica de negócio
"""

from .business_logic import BusinessRuleStrategy, HouseBusinessLogic
from .rules import BanheirosRule, QuartosRule, TamanhoRule

__all__ = [
    "HouseBusinessLogic",
    "BusinessRuleStrategy",
    "QuartosRule",
    "TamanhoRule",
    "BanheirosRule",
]

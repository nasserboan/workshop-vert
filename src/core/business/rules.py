"""
Definição de regras de negócio para predição de casas
"""

from abc import ABC, abstractmethod

from pydantic import BaseModel


class BusinessRuleStrategy(ABC):
    """
    Strategy pattern para aplicar regras de negócio.
    """

    @abstractmethod
    def apply(self, data: BaseModel) -> bool:
        """
        Aplica a regra de negócio.
        """


class QuartosRule(BusinessRuleStrategy):
    """
    Regra de negócio da quantidade de quartos.
    Se a quantidade de quartos for maior que 5, retorna True
    """

    def apply(self, data: BaseModel) -> bool:
        """
        Aplica a regra de negócio.
        """

        if data.quartos > 5:
            return True
        return False


class TamanhoRule(BusinessRuleStrategy):
    """
    Regra de negócio do tamanho da casa.
    Se o tamanho da casa for maior que 200, retorna True
    """

    def apply(self, data: BaseModel) -> bool:
        """
        Aplica a regra de negócio.
        """

        if data.tamanho > 200:
            return True
        return False


class BanheirosRule(BusinessRuleStrategy):
    """
    Regra de negócio da quantidade de banheiros.
    Se a quantidade de banheiros for maior que 4, retorna True
    """

    def apply(self, data: BaseModel) -> bool:
        """
        Aplica a regra de negócio.
        """

        if data.banheiros > 4:
            return True
        return False

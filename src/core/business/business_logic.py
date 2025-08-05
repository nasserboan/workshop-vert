"""
Modulo de carregamento e aplicação de regras de negócio

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

from pydantic import BaseModel

from .rules import BusinessRuleStrategy


class HouseBusinessLogic:
    """
    Classe para carregamento e aplicação de regras de negócio
    """

    def __init__(self):
        """
        Inicializa a classe
        """
        self.rules = []

    def add_rule(self, rule: BusinessRuleStrategy):
        """
        Adiciona uma regra de negócio
        """
        self.rules.append(rule)

        return self

    def apply_rules(self, data: BaseModel) -> list[int]:
        """
        Aplica as regras de negócio
        """

        results = []

        for rule in self.rules:
            result = rule.apply(data)
            results.append(result)

        return results

"""
Módulo de avaliação do modelo.

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

from sklearn.metrics import r2_score


class ModelEvaluator:
    def __init__(self, model, test_data: tuple):
        self.model = model
        self.test_data = test_data

    def run(self):
        """
        Executa a avaliação do modelo
        """
        x_test, y_test = self.test_data
        return r2_score(y_test, self.model.predict(x_test))

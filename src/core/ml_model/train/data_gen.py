"""
Módulo de geração de dados de treinamento.

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

import pandas as pd
from sklearn.datasets import make_regression

from config.settings import trainer_config


class DataGenerator:
    def __init__(self, config=None):
        self.config = config or trainer_config

    def run(self):
        data = make_regression(
            n_samples=self.config.gen_n_samples,
            n_features=self.config.gen_n_features,
            noise=self.config.gen_noise,
            random_state=self.config.random_state,
        )

        df = pd.DataFrame(data[0], columns=["quartos", "tamanho", "banheiros"]).assign(
            valor=data[1]
        )

        return df

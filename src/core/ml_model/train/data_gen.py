"""
Módulo de geração de dados de treinamento.

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

import pandas as pd
from sklearn.datasets import make_regression

from config.settings import TrainerConfig


class DataGenerator:
    """Classe para geração de dados de treinamento"""

    def __init__(self, trainer_config: TrainerConfig):
        """Inicializa o gerador de dados"""
        self.config = trainer_config

    def run(self):
        """Gera dados de treinamento"""

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

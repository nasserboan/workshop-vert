"""
Módulo de pré-processamento de dados.

Ele é responsável por:
- Separar os dados em conjuntos de treinamento e teste
- Normalizar os dados
- Salvar o objeto de pré-processamento

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

import os
import pickle
from datetime import datetime

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from config.settings import trainer_config


class DataPreprocessor:
    def __init__(self, data: pd.DataFrame, config=None):
        """
        Inicializa o pré-processador de dados

        Args:
            data: DataFrame com os dados de treinamento (incluindo target)
            config: Configurações (opcional)
        """
        self.data = data
        self.config = config or trainer_config

    def _split_data(self):
        """
        Separa os dados em conjuntos de treinamento e teste

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: Conjunto de treinamento e teste
        """

        x_train, x_test, y_train, y_test = train_test_split(
            self.data.drop(columns=["valor"]),
            self.data["valor"],
            test_size=self.config.test_size,
            random_state=self.config.random_state,
        )

        return (x_train, y_train), (x_test, y_test)

    def _normalize_data(self, x_train, x_test):
        """
        Normaliza os dados

        Args:
            x_train: Conjunto de treinamento
            x_test: Conjunto de teste
        """
        scaler = StandardScaler()
        scaled_x_train = scaler.fit_transform(x_train)
        scaled_x_test = scaler.transform(x_test)

        self.scaler = scaler

        return scaled_x_train, scaled_x_test

    def _save_scaler(self):
        """
        Salva o objeto de pré-processamento
        """
        path = f"models/{datetime.now().strftime('%Y%m%d')}/scaler.pkl"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(self.scaler, f)

    def run(self):
        """
        Executa o pré-processamento dos dados
        """
        train_data, test_data = self._split_data()

        x_train, y_train = train_data
        x_test, y_test = test_data

        scaled_x_train, scaled_x_test = self._normalize_data(x_train, x_test)
        self._save_scaler()

        return (scaled_x_train, y_train), (scaled_x_test, y_test)

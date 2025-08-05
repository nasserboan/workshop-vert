"""
Modelo de regressão para predição

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

import pickle

import pandas as pd
from loguru import logger


class HouseRegressor:

    def __init__(self, model_path: str):
        """Carrega o modelo e gera a predição"""
        self.model_path = model_path
        self.load_model()

    def load_model(self):
        """Carrega o modelo"""
        logger.info(f"Carregando modelo de {self.model_path}")
        try:
            with open(self.model_path, "rb") as f:
                self.model = pickle.load(f)
            logger.info("Modelo carregado com sucesso")
        except FileNotFoundError:
            logger.error(f"Arquivo de modelo não encontrado: {self.model_path}")
            raise
        except pickle.PickleError as e:
            logger.error(f"Erro ao deserializar modelo: {e}")
            raise
        except Exception as e:
            logger.error(f"Erro inesperado ao carregar modelo: {e}")
            raise

    def predict(self, scaled_data: pd.DataFrame):
        """Faz predição"""
        logger.info("Fazendo predição")
        try:
            prediction = self.model.predict(scaled_data)
            logger.info("Predição feita com sucesso")
            return prediction
        except Exception as e:
            logger.error(f"Erro ao fazer predição: {e}")
            raise e

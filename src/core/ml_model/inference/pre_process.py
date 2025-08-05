"""
Pré-processamento de dados para predição

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

import pickle

import pandas as pd
from loguru import logger


class HousePreProcessor:
    """Classe para pré-processamento de dados"""

    def __init__(self, scaler_path: str):
        """
        Carrega o scaler e executa o pré-processamento

        Args:
            scaler_path: Caminho para o arquivo de scaler
        """
        logger.info(f"Carregando scaler de {scaler_path}")
        try:
            with open(scaler_path, "rb") as f:
                self.scaler = pickle.load(f)
            logger.info("Scaler previamente treinado carregado com sucesso")
        except FileNotFoundError:
            logger.error(f"Arquivo de scaler não encontrado: {scaler_path}")
            raise
        except pickle.PickleError as e:
            logger.error(f"Erro ao deserializar scaler: {e}")
            raise
        except Exception as e:
            logger.error(f"Erro inesperado ao carregar scaler: {e}")
            raise

    def preprocess(self, data: pd.DataFrame):
        """
        Pré-processa os dados

        Args:
            data: Dados a serem pré-processados
        """
        logger.info("Pré-processando dados")
        scaled_data = self.scaler.transform(data)
        return scaled_data

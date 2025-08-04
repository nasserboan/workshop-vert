"""
Módulo de salvamento do modelo.

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

import json
import os
import pickle
from datetime import datetime

from loguru import logger


class ModelSaver:
    def __init__(self, model):
        self.model = model

    def run(self):
        """
        Executa o salvamento do modelo
        """
        try:
            model_name = self.model.__class__.__name__
            model_params = self.model.get_params()
            model_date = datetime.now().strftime("%Y%m%d")
            model_path = f"models/{model_name}/{model_date}"
            os.makedirs(model_path, exist_ok=True)
            with open(f"{model_path}/model_params.json", "w") as f:
                json.dump(model_params, f)
            with open(f"{model_path}/model.pkl", "wb") as f:
                pickle.dump(self.model, f)
            return True
        except Exception as e:
            logger.error(f"Erro ao salvar o modelo: {e}")
            return False

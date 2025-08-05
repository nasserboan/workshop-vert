"""
Serviço de predição de casas
"""

from loguru import logger

from config.settings import app_config

from ..api.models import PredictionRequest
from ..utils import pydantic_model_to_dataframe
from .business import HouseBusinessLogic, QuartosRule, TamanhoRule
from .ml_model import HousePreProcessor, HouseRegressor


class HousePredictorApp:
    def __init__(self, preprocessor=None, regressor=None):
        """Inicializa a aplicação de predição"""

        logger.info("Inicializando HousePredictorApp")
        self.house_logic = HouseBusinessLogic()

        self.preprocessor = preprocessor or HousePreProcessor(
            scaler_path=app_config.scaler_path
        )
        self.regressor = regressor or HouseRegressor(model_path=app_config.model_path)

    def _apply_business_rules(self, data: PredictionRequest) -> bool:
        """Aplica as regras de negócio"""
        logger.info("Aplicando regras de negócio")
        self.house_logic.add_rule(QuartosRule()).add_rule(TamanhoRule())
        business_rules = self.house_logic.apply_rules(data)
        return not any(business_rules)  # Retorna True se nenhuma regra foi violada

    def _preprocess_data(self, data: PredictionRequest):
        """Pré-processa os dados"""
        logger.info("Iniciando pré-processamento")
        dataframe = pydantic_model_to_dataframe(data)
        return self.preprocessor.preprocess(dataframe)

    def _make_prediction(self, processed_data):
        """Faz a predição"""
        logger.info("Fazendo predição")
        return self.regressor.predict(processed_data)

    def predict(self, data: PredictionRequest) -> float:
        """
        Faz o fluxo completo da aplicação
        """

        # 1. Aplicação das regras de negócio
        if not self._apply_business_rules(data):
            logger.error("Regras de negócio violadas")
            return -1

        # 2. Pré-processamento
        processed_data = self._preprocess_data(data)

        # 3. Predição
        prediction = self._make_prediction(processed_data)

        return prediction

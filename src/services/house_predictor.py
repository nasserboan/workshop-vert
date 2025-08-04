"""
Serviço de predição de casas
"""

from loguru import logger

from ..core.business_logic import HouseLogic
from ..core.ml_model.pre_process import PreProcessor
from ..core.ml_model.regressor import Regressor


class HousePredictorApp:
    """Aplicação de predição de casas"""

    def __init__(self):
        """Inicializa a aplicação de predição"""
        logger.info("Inicializando HousePredictorApp")
        self.house_logic = HouseLogic()
        self.preprocessor = PreProcessor()
        self.regressor = Regressor()

    def predict(self, data):
        """Faz predição completa"""
        # TODO: Implementar fluxo de predição
        logger.info("Iniciando predição")

        # 1. Validação de negócio
        self.house_logic.validate_input(data)

        # 2. Pré-processamento
        processed_data = self.preprocessor.preprocess(data)

        # 3. Predição
        prediction = self.regressor.predict(processed_data)

        return prediction

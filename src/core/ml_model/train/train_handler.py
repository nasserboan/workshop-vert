"""
Orquestrador de treinamento do modelo de predição de casas.

Esse módulo é responsável por orquestrar o treinamento do modelo de predição de casas.

Ele é responsável por:
- Gerar dados de treinamento
- Pré-processar dados
- Treinar o modelo
- Otimizar o modelo
- Avaliar o modelo
- Salvar o modelo

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

from loguru import logger

from config.settings import TrainerConfig

from .data_gen import DataGenerator
from .eval import ModelEvaluator
from .hpo import ModelHPO
from .pre_process import DataPreprocessor
from .saver import ModelSaver
from .train_model import ModelTrainer

logger.add("logs/train.log", level="INFO", rotation="10 MB")


class ModelOrchestrator:
    """Classe para treinamento do modelo de predição de casas"""

    def __init__(self, trainer_config: TrainerConfig):
        logger.info("Inicializando ModelTrainer")
        self.config = trainer_config

    def _generate_data(self):
        data_generator = DataGenerator(self.config)
        return data_generator.run()

    def _preprocess_data(self, data):
        preprocessor = DataPreprocessor(data, self.config)
        return preprocessor.run()

    def _train_model(self, data):
        model_trainer = ModelTrainer(data, self.config)
        return model_trainer.run()

    def _optimize_model(self, model, train_data):
        hpo = ModelHPO(model, train_data, self.config)
        return hpo.run()

    def _evaluate_model(self, model, test_data):
        evaluator = ModelEvaluator(model, test_data)
        return evaluator.run()

    def _save_model(self, model):
        saver = ModelSaver(model)
        return saver.run()

    def run(self):
        """
        Executa o treinamento do modelo de predição de casas
        """
        logger.info("Iniciando treinamento do modelo de predição de casas")
        data = self._generate_data()
        logger.info("Dados gerados com sucesso")
        train_data, test_data = self._preprocess_data(data)
        logger.info("Dados pré-processados com sucesso")
        model = self._train_model(train_data)
        logger.info("Modelo treinado com sucesso")
        optimized_model = self._optimize_model(model, train_data)
        logger.info("Modelo otimizado com sucesso")
        score = self._evaluate_model(optimized_model, test_data)
        logger.info(f"Modelo avaliado com sucesso com score de {score}")
        if self._save_model(optimized_model):
            logger.info("Modelo salvo com sucesso")
        else:
            logger.error("Erro ao salvar o modelo")
        logger.info("Treinamento do modelo de predição de casas concluído com sucesso")


if __name__ == "__main__":
    config = TrainerConfig()
    orchestrator = ModelOrchestrator(config)
    orchestrator.run()

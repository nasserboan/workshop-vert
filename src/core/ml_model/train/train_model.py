"""
Módulo de treinamento do modelo de predição de casas.

Ele é responsável por:
- Treinar o modelo
- Salvar o modelo

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

from sklearn.ensemble import RandomForestRegressor

from config.settings import trainer_config


class ModelTrainer:
    """Classe para treinamento do modelo de predição de casas"""

    def __init__(self, train_data: tuple, config=None):
        """
        Inicializa o treinador

        Args:
            train_data: Tuple com os dados de treinamento
            config: Configurações do treinamento (opcional)
        """
        self.config = config or trainer_config
        self.train_data = train_data

    def _train_model(self):
        """
        Treina o modelo
        """
        x_train, y_train = self.train_data
        model = RandomForestRegressor(random_state=self.config.random_state)
        model.fit(x_train, y_train)
        return model

    def run(self):
        """
        Executa o treinamento do modelo

        Returns:
            Modelo treinado
        """
        model = self._train_model()
        return model

"""
Módulo de otimização de hiperparâmetros.

Ele é responsável por:
- Otimizar os hiperparâmetros do modelo
- Recriar o modelo com os melhores hiperparâmetros

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

import optuna
from sklearn.metrics import r2_score

from config.settings import TrainerConfig


class ModelHPO:
    def __init__(self, model, train_data: tuple, config: TrainerConfig):
        self.model = model
        self.train_data = train_data
        self.config = config

    def objective(self, trial, model, train_data: tuple):
        """
        Função objetivo para a otimização de hiperparâmetros
        """
        x_train, y_train = train_data
        params = {
            "n_estimators": trial.suggest_int("n_estimators", 100, 1000, step=100),
            "max_depth": trial.suggest_int("max_depth", 1, 50),
            "min_samples_leaf": trial.suggest_float("min_samples_leaf", 0.01, 0.5),
        }

        model.set_params(**params)
        model.fit(x_train, y_train)
        return r2_score(y_train, model.predict(x_train))

    def _optimize_model(self, model, train_data: tuple):
        """
        Otimiza os hiperparâmetros do modelo
        """

        study = optuna.create_study(direction="maximize")
        study.optimize(
            lambda trial: self.objective(trial, model, train_data),
            n_trials=self.config.optuna_n_trials,
            show_progress_bar=True,
        )

        return study.best_params

    def run(self):
        """
        Executa a otimização de hiperparâmetros
        """

        best_params = self._optimize_model(self.model, self.train_data)
        self.model.set_params(**best_params)
        self.model.fit(self.train_data[0], self.train_data[1])

        return self.model

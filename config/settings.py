"""
Configurações da aplicação usando Pydantic
"""

from pydantic_settings import BaseSettings


class TrainerConfig(BaseSettings):
    """
    Configurações de treinamento
    """
    
    gen_n_samples: int = 100
    gen_n_features: int = 3
    gen_noise: float = 0.1
    random_state: int = 42
    test_size: float = 0.2
    optuna_n_trials: int = 100


class AppConfig(BaseSettings):
    """
    Configurações da aplicação
    """
    
    model_date: str = "20250805"
    models_path: str = "src/models"
    
    @property
    def scaler_path(self) -> str:
        return f"{self.models_path}/{self.model_date}/scaler.pkl"
    
    @property
    def model_path(self) -> str:
        return f"{self.models_path}/{self.model_date}/RandomForestRegressor/model.pkl"


# Instâncias globais das configurações
trainer_config = TrainerConfig()
app_config = AppConfig()

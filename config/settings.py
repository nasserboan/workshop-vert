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


# Instância global das configurações
settings = TrainerConfig()

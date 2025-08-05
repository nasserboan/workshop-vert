"""
Esse módulo contém as rotas da API.

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br

"""

import time

from fastapi import APIRouter

from ..core.house_predictor import HousePredictorApp
from .models import PredictionRequest, PredictionResponse

router = APIRouter()


@router.get("/health", tags=["health"])
def health_check():
    """health check"""
    return {
        "status": "healthy",
        "service": "api-predicao-casas",
        "version": "1.0.0",
        "timestamp": time.time(),
    }


@router.get("/")
def root():
    """
    Endpoint raiz da API
    """
    return {
        "message": "API funcionando! Entre em /docs para ver a documentação da API."
    }


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    """
    Endpoint para predição.

    Recebe dados de uma casa e retorna a previsão de seu valor.

    Args:
        request: Dados da casa a ser predita.

    """
    predictor = HousePredictorApp()
    prediction = predictor.predict(request)

    return PredictionResponse(prediction=prediction)

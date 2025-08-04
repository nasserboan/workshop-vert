"""
Esse módulo contém as rotas da API.

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br

"""

from fastapi import APIRouter

from models import PredictionRequest, PredictionResponse

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    """
    Endpoint para predição.

    Recebe dados de uma casa e retorna a previsão de seu valor.

    Args:
        request: Dados da casa a ser predita.

    """
    # TODO: Implementar lógica de predição
    return PredictionResponse(prediction=0.0)

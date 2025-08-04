"""
Esse módulo contém os modelos Pydantic para a API.

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    """
    Modelo para requisição de predição.

    Recebe dados de uma casa e retorna a previsão de seu valor.

    Args:
        quartos: Número de quartos.
        tamanho: Tamanho da casa em metros quadrados.
        banheiros: Número de banheiros.
    """

    quartos: int = Field(..., description="Número de quartos")
    tamanho: float = Field(..., description="Tamanho da casa em metros quadrados")
    banheiros: int = Field(..., description="Número de banheiros")


class PredictionResponse(BaseModel):
    """
    Modelo para resposta de predição.

    Retorna a previsão de valor da casa.

    Args:
        prediction: Previsão de valor da casa.
    """

    prediction: float

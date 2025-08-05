"""
Criação da API de predição de casas

A API é responsável por receber dados de uma casa e retornar a previsão de seu valor.

Versão: 1.0.0
Data: 06/08/2025
Autor: Nasser Boan
nasser.boan@vert.com.br
"""

import time

from fastapi import FastAPI, Request
from loguru import logger

from .api import router

# Configuração do logger
logger.add("logs/app.log", rotation="10 MB", retention="7 days", level="INFO")

# Criação da aplicação FastAPI
app = FastAPI(
    title="API de predição de casas",
    version="1.0.0",
    description="API de predição de casas",
)


@app.middleware("http")
async def request_logging_middleware(request: Request, call_next):
    """Middleware para logging de requisições"""
    start_time = time.time()

    # Processa a requisição
    response = await call_next(request)

    # Calcula duração
    duration = time.time() - start_time

    # Loga informações da requisição
    logger.info(
        f"{request.method} {request.url.path} - {response.status_code} - {duration:.3f}s"
    )

    return response


# Inclui as rotas da API
app.include_router(router, prefix="/api/v1", tags=["api"])


@app.get("/health", tags=["health"])
def health_check():
    """Endpoint de verificação de saúde"""
    return {
        "status": "healthy",
        "service": "api-predicao-casas",
        "version": "1.0.0",
        "timestamp": time.time(),
    }

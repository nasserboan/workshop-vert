# Boas Práticas de Clean Code - Exemplos Práticos

Este documento apresenta algumas boas práticas de clean code aplicadas neste projeto de API de predição de casas. Vou mostrar exemplos reais do código e explicar como eles contribuem para a qualidade e manutenibilidade do software.

## 1. Nomes Significativos e Descritivos

### Nomes que revelam a intenção

```python
# src/api/models.py
class PredictionRequest(BaseModel):
    """
    Modelo para requisição de predição.
    """
    quartos: int = Field(..., gt=0, le=10, description="Número de quartos")
    tamanho: float = Field(..., gt=0, le=1000, description="Tamanho da casa em metros quadrados")
    banheiros: int = Field(..., gt=0, le=10, description="Número de banheiros")
```

Os nomes das variáveis e classes são autoexplicativos. `PredictionRequest` deixa claro que é um modelo para requisições de predição, e os campos `quartos`, `tamanho` e `banheiros` são intuitivos.

### Métodos com nomes que descrevem a ação

```python
# src/core/house_predictor.py
def _apply_business_rules(self, data: PredictionRequest) -> bool:
    """Aplica as regras de negócio"""
    
def _preprocess_data(self, data: PredictionRequest):
    """Pré-processa os dados"""
    
def _make_prediction(self, processed_data):
    """Faz a predição"""
```

Cada método tem um nome que deixa claro o que ele faz, facilitando a leitura e compreensão do código.

## 2. Funções Pequenas e com Responsabilidade Única

### Métodos focados em uma única responsabilidade

```python
# src/core/house_predictor.py
def predict(self, data: PredictionRequest) -> float:
    """
    Faz o fluxo completo da aplicação
    """
    # 1. Aplicação das regras de negócio
    if not self._apply_business_rules(data):
        logger.error("Regras de negócio violadas")
        return -1

    # 2. Pré-processamento
    processed_data = self._preprocess_data(data)

    # 3. Predição
    prediction = self._make_prediction(processed_data)

    return prediction
```

O método `predict` orquestra o fluxo principal, mas delega responsabilidades específicas para métodos menores e mais focados. Cada método tem uma única responsabilidade bem definida.

## 3. Comentários Significativos

### Comentários que explicam o "porquê", não o "o quê"

```python
# src/main.py
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
```

Os comentários explicam o propósito de cada seção do código, não apenas o que o código faz.

## 4. Estrutura de Diretórios Organizada

### Separação clara de responsabilidades

```
src/
├── api/           # Camada de API e endpoints
├── core/          # Lógica de negócio principal
├── utils/         # Utilitários reutilizáveis
├── models/        # Modelos de ML
└── services/      # Serviços externos
```

A estrutura de diretórios reflete a arquitetura do sistema, facilitando a navegação e manutenção.

## 5. Uso de Design Patterns

### Strategy Pattern para regras de negócio

```python
# src/core/business/rules.py
class BusinessRuleStrategy(ABC):
    """
    Strategy pattern para aplicar regras de negócio.
    """
    @abstractmethod
    def apply(self, data: BaseModel) -> bool:
        """
        Aplica a regra de negócio.
        """

class QuartosRule(BusinessRuleStrategy):
    """
    Regra de negócio da quantidade de quartos.
    Se a quantidade de quartos for maior que 5, retorna True
    """
    def apply(self, data: BaseModel) -> bool:
        if data.quartos > 5:
            return True
        return False
```

O uso do Strategy Pattern permite adicionar novas regras de negócio sem modificar o código existente, seguindo o princípio Open/Closed.

## 6. Validação de Dados com Pydantic

### Validação automática e documentação

```python
# src/api/models.py
class PredictionRequest(BaseModel):
    quartos: int = Field(..., gt=0, le=10, description="Número de quartos")
    tamanho: float = Field(..., gt=0, le=1000, description="Tamanho da casa em metros quadrados")
    banheiros: int = Field(..., gt=0, le=10, description="Número de banheiros")
```

O uso do Pydantic garante validação automática dos dados de entrada, documentação clara e type hints, reduzindo bugs e melhorando a experiência do desenvolvedor.

## 7. Logging Estruturado

### Logs informativos e estruturados

```python
# src/main.py
logger.add("logs/app.log", rotation="10 MB", retention="7 days", level="INFO")

# src/core/house_predictor.py
logger.info("Inicializando HousePredictorApp")
logger.info("Aplicando regras de negócio")
logger.info("Iniciando pré-processamento")
logger.info("Fazendo predição")
```

O uso do Loguru com configuração de rotação e retenção, além de logs informativos em pontos estratégicos, facilita o debugging e monitoramento.

## 8. Configuração Centralizada

### Configurações organizadas

```python
# src/core/house_predictor.py
from config.settings import app_config

self.preprocessor = preprocessor or HousePreProcessor(
    scaler_path=app_config.scaler_path
)
self.regressor = regressor or HouseRegressor(model_path=app_config.model_path)
```

As configurações são centralizadas, facilitando mudanças e evitando hardcoding de valores.

## 9. Tratamento de Erros

### Tratamento explícito de casos de erro

```python
# src/core/house_predictor.py
def predict(self, data: PredictionRequest) -> float:
    # 1. Aplicação das regras de negócio
    if not self._apply_business_rules(data):
        logger.error("Regras de negócio violadas")
        return -1
```

O código trata explicitamente casos onde as regras de negócio são violadas, retornando um valor específico e logando o erro.

## 10. Testabilidade

### Injeção de dependências para facilitar testes

```python
# src/core/house_predictor.py
def __init__(self, preprocessor=None, regressor=None):
    """Inicializa a aplicação de predição"""
    self.preprocessor = preprocessor or HousePreProcessor(
        scaler_path=app_config.scaler_path
    )
    self.regressor = regressor or HouseRegressor(model_path=app_config.model_path)
```

A possibilidade de injetar dependências facilita a criação de testes unitários, permitindo mockar componentes externos.

## 11. Documentação de API

### Documentação automática com FastAPI

```python
# src/main.py
app = FastAPI(
    title="API de predição de casas",
    version="1.0.0",
    description="API de predição de casas",
)

# src/api/routes.py
@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    """
    Endpoint para predição.

    Recebe dados de uma casa e retorna a previsão de seu valor.

    Args:
        request: Dados da casa a ser predita.
    """
```

O uso do FastAPI com Pydantic gera automaticamente documentação interativa da API, facilitando o uso e testes.

## 12. Ferramentas de Qualidade de Código

### Configuração de linters e formatters

```toml
# pyproject.toml
[tool.ruff]
target-version = "py312"
line-length = 88
lint.select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
]

[tool.black]
line-length = 88
target-version = ['py312']
```

A configuração de ferramentas como Ruff e Black garante consistência no estilo de código e identifica problemas potenciais.

## Conclusão

Este projeto demonstra várias boas práticas de clean code que contribuem para:

- **Legibilidade**: Nomes descritivos e estrutura clara
- **Manutenibilidade**: Separação de responsabilidades e design patterns
- **Testabilidade**: Injeção de dependências e funções pequenas
- **Robustez**: Validação de dados e tratamento de erros
- **Documentação**: Comentários significativos e documentação automática

A aplicação dessas práticas torna o código mais profissional, fácil de entender e manter, além de facilitar a colaboração em equipe. 
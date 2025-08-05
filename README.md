# API de Predição de Casas

Uma API RESTful desenvolvida em FastAPI para predição de valores de casas usando machine learning.

## Características

- **FastAPI**: Framework moderno e rápido para APIs
- **Pydantic**: Validação de dados e serialização
- **Scikit-learn**: Modelo de machine learning (Random Forest)
- **Estrutura modular**: Organização clara do código
- **Logging estruturado**: Sistema de logs configurável
- **Documentação automática**: Swagger UI e ReDoc
- **Tratamento de erros**: Middleware para exceções
- **Modelo treinado**: Random Forest para predição de valores

## Estrutura do Projeto

```
api-simples/
├── pyproject.toml          # Configuração do projeto
├── requirements.txt        # Dependências
├── .gitignore             # Arquivos ignorados pelo Git
├── README.md              # Este arquivo
├── src/                   # Código fonte
│   ├── __init__.py
│   ├── main.py            # Aplicação principal
│   ├── api/               # Camada de API
│   │   ├── __init__.py
│   │   ├── routes.py      # Rotas da API
│   │   └── models.py      # Modelos Pydantic
│   ├── core/              # Lógica de negócio
│   │   ├── __init__.py
│   │   ├── house_predictor.py  # Orquestrador de predição
│   │   ├── business/      # Regras de negócio
│   │   └── ml_model/      # Modelo de machine learning
│   │       ├── inference/ # Inferência do modelo
│   │       └── train/     # Treinamento do modelo
│   ├── models/            # Modelos treinados
│   │   └── 20250805/      # Modelo da data específica
│   ├── services/          # Serviços externos
│   │   └── __init__.py
│   └── utils/             # Utilitários
│       └── __init__.py
├── config/                # Configurações
│   └── settings.py        # Configurações da aplicação
├── logs/                  # Logs da aplicação
└── tests/                 # Testes
    └── __init__.py
```

## Instalação

### Pré-requisitos

- Python 3.12+
- pip ou uv

### Configuração Rápida

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd api-simples
   ```

2. **Crie um ambiente virtual e instale dependências:**
   ```bash
   uv sync
   ```

4. **Execute a aplicação:**
   ```bash
   make run-api
   ```

5. **Acesse a documentação:**
   - Swagger UI: http://localhost:8000/docs

## Executando a Aplicação

### Desenvolvimento

```bash
# Com hot reload
make run-api
```

### Produção

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## Documentação da API

### Endpoints Principais

- `GET /api/v1/` - Endpoint raiz
- `GET /api/v1/health` - Verificação de saúde
- `POST /api/v1/predict` - Predição de valor de casa

### Endpoint de Predição

O endpoint `/api/v1/predict` recebe dados de uma casa e retorna a previsão de seu valor.

**Request:**
```json
{
  "quartos": 3,
  "tamanho": 120.5,
  "banheiros": 2
}
```

**Response:**
```json
{
  "prediction": 250000.0
}
```

### Exemplo de Uso

```bash
# Predição de valor de casa
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"quartos": 3, "tamanho": 120.5, "banheiros": 2}'

# Health check
curl http://localhost:8000/health
```

## Modelo de Machine Learning

O projeto utiliza um modelo Random Forest treinado para predição de valores de casas baseado em:
- Número de quartos
- Tamanho em metros quadrados
- Número de banheiros

O modelo está salvo em `src/models/20250805/` e inclui:
- `scaler.pkl`: Scaler para normalização dos dados
- `RandomForestRegressor/model.pkl`: Modelo treinado
- `RandomForestRegressor/model_params.json`: Parâmetros do modelo

## Regras de Negócio

O sistema aplica regras de negócio antes da predição:
- Validação de número de quartos
- Validação de tamanho da casa
- Validação de número de banheiros

## Logs

Os logs são salvos em `logs/app.log` e também exibidos no console.

### Níveis de Log

- `INFO`: Informações gerais da aplicação
- `ERROR`: Erros que impedem operações específicas


## Configuração

### Configurações de Treinamento

As configurações estão em `config/settings.py`:

- `gen_n_samples`: Número de amostras para geração de dados
- `gen_n_features`: Número de features
- `gen_noise`: Ruído nos dados
- `random_state`: Seed para reprodutibilidade
- `test_size`: Proporção de dados de teste
- `optuna_n_trials`: Número de tentativas para otimização

## Makefile

O projeto inclui um Makefile com comandos úteis para desenvolvimento:

### Comandos Disponíveis

```bash
# Ver todos os comandos disponíveis
make help

# Treinar o modelo de machine learning
make train

# Formatar o código com black
make format

# Corrigir problemas de linting automaticamente
make fix

# Verificar qualidade do código
make lint

# Executar format + fix + lint
make quality

# Executar a API em modo desenvolvimento
make run-api
```

### Uso dos Comandos

- **`make train`**: Treina o modelo Random Forest usando os dados gerados
- **`make format`**: Formata todo o código fonte usando Black
- **`make fix`**: Corrige automaticamente problemas de linting detectados pelo Ruff
- **`make lint`**: Verifica a qualidade do código sem fazer correções
- **`make quality`**: Executa formatação, correção e verificação em sequência
- **`make run-api`**: Inicia a API em modo desenvolvimento com hot reload

### Exemplo de Fluxo de Desenvolvimento

```bash
# 1. Fazer alterações no código
# 2. Verificar e corrigir qualidade
make quality

# 3. Treinar modelo (se necessário)
make train

# 4. Executar API
make run-api
```
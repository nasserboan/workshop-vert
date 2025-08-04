# API Simples

Uma API RESTful desenvolvida em FastAPI para demonstração de boas práticas de desenvolvimento Python.

## 🚀 Características

- **FastAPI**: Framework moderno e rápido para APIs
- **Pydantic**: Validação de dados e serialização
- **Estrutura modular**: Organização clara do código
- **Testes automatizados**: Cobertura completa com pytest
- **Logging estruturado**: Sistema de logs configurável
- **Configuração flexível**: Suporte a YAML e variáveis de ambiente
- **Documentação automática**: Swagger UI e ReDoc
- **Tratamento de erros**: Middleware para exceções
- **CORS configurado**: Suporte a requisições cross-origin
- **Scripts de automação**: Setup e deploy automatizados

## 📁 Estrutura do Projeto

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
│   │   └── business_logic.py
│   ├── services/          # Serviços externos
│   │   ├── __init__.py
│   │   └── external_api.py
│   └── utils/             # Utilitários
│       ├── __init__.py
│       ├── config.py      # Gerenciamento de configurações
│       └── logger.py      # Sistema de logging
├── tests/                 # Testes
│   ├── __init__.py
│   ├── test_api.py        # Testes da API
│   └── test_core.py       # Testes da lógica de negócio
├── config/                # Configurações
│   └── settings.yaml      # Configurações da aplicação
├── docs/                  # Documentação
│   └── api.md             # Documentação da API
└── scripts/               # Scripts de automação
    ├── setup.sh           # Script de configuração
    └── deploy.sh          # Script de deploy
```

## 🛠️ Instalação

### Pré-requisitos

- Python 3.8+
- pip
- Git

### Configuração Rápida

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd api-simples
   ```

2. **Execute o script de configuração:**
   ```bash
   chmod +x scripts/setup.sh
   ./scripts/setup.sh
   ```

3. **Ative o ambiente virtual:**
   ```bash
   source .venv/bin/activate
   ```

4. **Execute a aplicação:**
   ```bash
   python -m src.main
   ```

5. **Acesse a documentação:**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Configuração Manual

Se preferir configurar manualmente:

1. **Crie um ambiente virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Instale dependências de desenvolvimento:**
   ```bash
   pip install pytest pytest-cov black flake8 mypy
   ```

4. **Crie os diretórios necessários:**
   ```bash
   mkdir -p logs data
   ```

## 🚀 Executando a Aplicação

### Desenvolvimento

```bash
# Com hot reload
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Ou usando o módulo Python
python -m src.main
```

### Produção

```bash
# Usando o script de deploy
./scripts/deploy.sh deploy

# Ou manualmente
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## 🧪 Testes

### Executar todos os testes

```bash
pytest
```

### Executar com cobertura

```bash
pytest --cov=src --cov-report=html --cov-report=term
```

### Executar testes específicos

```bash
# Testes da API
pytest tests/test_api.py

# Testes da lógica de negócio
pytest tests/test_core.py

# Testes com verbose
pytest -v
```

## 📊 Qualidade do Código

### Formatação

```bash
# Verificar formatação
black --check src/ tests/

# Formatar código
black src/ tests/
```

### Linting

```bash
# Verificar qualidade
flake8 src/ tests/ --max-line-length=88 --ignore=E203,W503
```

### Verificação de tipos

```bash
# Verificar tipos
mypy src/ --ignore-missing-imports
```

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Configurações de ambiente
APP_NAME=api-simples
DEBUG=True
PORT=8000
HOST=0.0.0.0

# Configurações de banco de dados
DATABASE_URL=sqlite:///./data/app.db

# Configurações de API externa
EXTERNAL_API_URL=https://api.exemplo.com
EXTERNAL_API_KEY=your_api_key_here

# Configurações de logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# Configurações de segurança
SECRET_KEY=your-secret-key-change-in-production
```

### Arquivo de Configuração YAML

O arquivo `config/settings.yaml` contém configurações detalhadas da aplicação.

## 📚 Documentação da API

### Endpoints Principais

- `GET /` - Endpoint raiz
- `GET /health` - Verificação de saúde
- `GET /config` - Configurações (apenas em debug)

### Endpoints de Itens

- `GET /api/v1/items` - Lista todos os itens
- `GET /api/v1/items/{id}` - Busca item por ID
- `POST /api/v1/items` - Cria novo item
- `PUT /api/v1/items/{id}` - Atualiza item
- `DELETE /api/v1/items/{id}` - Remove item

### Exemplo de Uso

```bash
# Listar itens
curl http://localhost:8000/api/v1/items

# Criar item
curl -X POST http://localhost:8000/api/v1/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Teste", "price": 99.99}'

# Buscar item
curl http://localhost:8000/api/v1/items/1
```

## 🐳 Docker

### Construir imagem

```bash
docker build -t api-simples .
```

### Executar container

```bash
docker run -p 8000:8000 api-simples
```

### Usando o script

```bash
# Construir imagem
./scripts/deploy.sh docker

# Executar no Docker
./scripts/deploy.sh run-docker

# Parar aplicação
./scripts/deploy.sh stop-docker
```

## 📝 Logs

Os logs são salvos em `logs/app.log` e também exibidos no console.

### Níveis de Log

- `DEBUG`: Informações detalhadas para desenvolvimento
- `INFO`: Informações gerais da aplicação
- `WARNING`: Avisos que não impedem a execução
- `ERROR`: Erros que impedem operações específicas
- `CRITICAL`: Erros críticos que podem afetar a aplicação

## 🔍 Monitoramento

### Health Check

```bash
curl http://localhost:8000/health
```

### Métricas

Em modo debug, o endpoint `/config` fornece informações sobre a configuração.

## 🚀 Deploy

### Deploy Local

```bash
./scripts/deploy.sh deploy-local
```

### Deploy Completo

```bash
./scripts/deploy.sh deploy
```

### Verificar Status

```bash
./scripts/deploy.sh status
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código

- Use Black para formatação
- Siga as convenções PEP 8
- Escreva testes para novas funcionalidades
- Mantenha a cobertura de testes acima de 80%

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Se você encontrar algum problema ou tiver dúvidas:

1. Verifique a documentação
2. Execute os testes para verificar se tudo está funcionando
3. Abra uma issue no repositório

## 🔄 Changelog

### v1.0.0
- Implementação inicial da API
- Sistema de logging configurável
- Testes automatizados
- Documentação completa
- Scripts de automação

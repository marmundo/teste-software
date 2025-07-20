# Sistema de Descontos

Este projeto implementa um sistema de cálculo de descontos em Python com diferentes critérios de aplicação, demonstrando conceitos de cobertura de testes (C0, C1 e C2/MC-DC).

## Estrutura do Projeto

```
teste-software/
├── src/                              # Código fonte
│   ├── sistema_descontos.py          # Funções básicas de desconto (C0 e C1)
│   └── sistema_descontos_avancado.py # Função avançada com múltiplas condições (C2)
├── test/                             # Testes automatizados
│   ├── test_calcula_desconto_c0.py   # Testes para cobertura C0
│   ├── test_descontos_c1.py          # Testes para cobertura C1
│   └── test_descontos_avancado_c2.py # Testes para cobertura C2/MC-DC
├── requirements.txt                  # Dependências do projeto
├── htmlcov/                          # Relatórios HTML de cobertura (gerados)
└── README.md                         # Este arquivo
```

## Funcionalidades

### 🔸 Sistema Básico (C0/C1)
- **`calcular_desconto_c0`**: Aplica 10% de desconto para preços acima de R$ 100
- **`calcular_desconto_c1`**: Mesma lógica, com documentação de pontos de decisão

### 🔸 Sistema Avançado (C2/MC-DC)
- **`calcular_desconto_c2`**: Aplica 15% de desconto apenas se:
  - Preço > R$ 500 **E**
  - Cliente for VIP

## Tipos de Cobertura Demonstrados

| Tipo | Descrição | Arquivo de Teste |
|------|-----------|------------------|
| **C0** | Cobertura de comandos/statements | `test_calcula_desconto_c0.py` |
| **C1** | Cobertura de decisões/branches | `test_descontos_c1.py` |
| **C2/MC-DC** | Cobertura de condições modificadas | `test_descontos_avancado_c2.py` |

## Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

## Setup do Projeto

### 1. Clone ou baixe o projeto

```bash
cd /caminho/para/seu/workspace
```

### 2. Crie um ambiente virtual (recomendado)

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# No macOS/Linux:
source venv/bin/activate

# No Windows:
# venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute os testes

Para executar todos os testes:

```bash
pytest
```

Para executar testes com mais detalhes:

```bash
pytest -v
```

Para executar testes com coverage:

```bash
pytest --cov=src
```

Para executar testes com coverage e gerar relatório HTML:

```bash
pytest --cov=src --cov-report=html
```

Para executar testes com coverage e mostrar linhas não cobertas:

```bash
pytest --cov=src --cov-report=term-missing
```

Para gerar relatório HTML de coverage (abre no navegador):

```bash
pytest --cov=src --cov-report=html
```

> **Nota**: O relatório HTML será gerado na pasta `htmlcov/`. Para visualizar, abra o arquivo `htmlcov/index.html` no seu navegador.

## Como usar

### Exemplo de uso das funções de desconto:

```python
from src.sistema_descontos import calcular_desconto_c0, calcular_desconto_c1
from src.sistema_descontos_avancado import calcular_desconto_c2

# Sistema básico - desconto de 10%
preco_baixo = 80
preco_alto = 200

resultado_c0 = calcular_desconto_c0(preco_alto)
print(f"C0 - Preço: R$ {preco_alto} → Final: R$ {resultado_c0}")
# Output: C0 - Preço: R$ 200 → Final: R$ 180.0

# Sistema avançado - desconto de 15% para VIP
preco_vip = 600
eh_cliente_vip = True

resultado_c2 = calcular_desconto_c2(preco_vip, eh_cliente_vip)
print(f"C2 - Preço: R$ {preco_vip}, VIP: {eh_cliente_vip} → Final: R$ {resultado_c2}")
# Output: C2 - Preço: R$ 600, VIP: True → Final: R$ 510.0
```

## Executando Testes

### Executar todos os testes:
```bash
pytest
```

### Executar testes específicos por cobertura:
```bash
# Testes C0 (cobertura de comandos)
pytest test/test_calcula_desconto_c0.py -v

# Testes C1 (cobertura de decisões)
pytest test/test_descontos_c1.py -v

# Testes C2/MC-DC (cobertura de condições)
pytest test/test_descontos_avancado_c2.py -v
```

### Executar testes com relatório detalhado:
```bash
pytest -v --tb=short
```

### Gerar relatório HTML de coverage:
```bash
pytest --cov=src --cov-report=html
```

Após executar o comando acima, você pode:
1. Abrir o arquivo `htmlcov/index.html` no navegador
2. Ou usar o comando: `open htmlcov/index.html` (macOS) ou `start htmlcov/index.html` (Windows)

### Executar testes com coverage específico:
```bash
# Coverage apenas do sistema básico
pytest test/test_calcula_desconto_c0.py test/test_descontos_c1.py --cov=src.sistema_descontos

# Coverage apenas do sistema avançado
pytest test/test_descontos_avancado_c2.py --cov=src.sistema_descontos_avancado
```

## Desenvolvimento

### Adicionando Novos Testes

Para adicionar novos testes, siga a estrutura:

1. Crie arquivos de teste na pasta `test/`
2. Nomeie os arquivos iniciando com `test_`
3. Nomeie as funções de teste iniciando com `test_`
4. Use `assert` para validar os resultados esperados

### Exemplos de Testes por Tipo de Cobertura:

#### **Cobertura C0 (Comandos):**
```python
def test_comando_executado():
    """Garante que todos os comandos são executados pelo menos uma vez."""
    assert calcular_desconto_c0(200) == 180.0
```

#### **Cobertura C1 (Decisões):**
```python
def test_decisao_verdadeira():
    """Testa o caminho TRUE da decisão."""
    assert calcular_desconto_c1(200) == 180.0

def test_decisao_falsa():
    """Testa o caminho FALSE da decisão."""
    assert calcular_desconto_c1(50) == 50.0
```

#### **Cobertura C2/MC-DC (Condições):**
```python
def test_condicao_a_verdadeira_b_falsa():
    """Testa A=True, B=False → Resultado=False"""
    assert calcular_desconto_c2(600, False) == 600

def test_condicao_a_falsa_b_verdadeira():
    """Testa A=False, B=True → Resultado=False"""
    assert calcular_desconto_c2(400, True) == 400

def test_condicao_a_verdadeira_b_verdadeira():
    """Testa A=True, B=True → Resultado=True"""
    assert calcular_desconto_c2(800, True) == 680

def test_condicao_a_falsa_b_falsa():
    """Testa A=False, B=False → Resultado=False"""
    assert calcular_desconto_c2(300, False) == 300
```

## Estrutura de Testes

Os testes seguem o padrão **AAA** (Arrange, Act, Assert):
- **Arrange**: Preparação dos dados de entrada
- **Act**: Execução da função a ser testada
- **Assert**: Verificação do resultado esperado

## Conceitos de Cobertura

### 📊 **C0 - Cobertura de Comandos**
- Garante que cada linha de código seja executada pelo menos uma vez
- **Meta**: 100% das instruções executadas

### 🔀 **C1 - Cobertura de Decisões**
- Garante que cada ponto de decisão tenha ambos os caminhos (True/False) testados
- **Meta**: 100% dos branches executados

### 🎯 **C2/MC-DC - Cobertura de Condições**
- Garante que cada condição afete independentemente o resultado da decisão
- **Meta**: Cada condição deve ser testada de forma que sua mudança altere o resultado

## Contribuindo

1. Adicione testes para novas funcionalidades
2. Mantenha a cobertura de testes alta (objetivo: 100%)
3. Execute os testes antes de fazer commits
4. Documente as funções com docstrings claras
5. Siga os padrões de cobertura apropriados (C0, C1, C2)

## Resultados de Cobertura Esperados

Ao executar `pytest --cov=src --cov-report=term-missing`, você deve ver:

```
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
src/sistema_descontos.py               10      0   100%
src/sistema_descontos_avancado.py      5      0   100%
-----------------------------------------------------------------
TOTAL                                  15      0   100%
```

## Licença

Este projeto é apenas para fins educacionais e de demonstração de técnicas de teste de software.

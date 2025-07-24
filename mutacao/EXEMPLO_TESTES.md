# Exemplo: Como Matar os Mutantes Sobreviventes

Baseado nos resultados do mutation testing, aqui estão exemplos de como adicionar testes para matar os mutantes que sobreviveram.

## Mutante 1: `nota > 100` → `nota >= 100`

**Problema**: Não há teste para `nota = 100`

**Solução**: Adicionar teste para verificar que 100 é uma nota válida
```python
def test_deve_retornar_aprovado_para_nota_100():
    assert classificar_nota(100) == "Aprovado"
```

## Mutante 2: `nota < 0` → `nota <= 0`

**Problema**: Não há teste para `nota = 0`

**Solução**: Adicionar teste para verificar que 0 é uma nota válida
```python
def test_deve_retornar_reprovado_para_nota_0():
    assert classificar_nota(0) == "Reprovado"
```

## Mutante 3: `nota >= 60` → `nota > 60`

**Problema**: Não há teste específico para `nota = 60`

**Solução**: Você já tem, mas pode reforçar:
```python
def test_deve_retornar_aprovado_para_nota_limite_60():
    assert classificar_nota(60) == "Aprovado"
```

## Teste Completo Recomendado

Adicione estes testes ao seu `test_classificador.py`:

```python
from classificador import classificar_nota


def test_deve_retornar_aprovado_para_nota_alta():
    assert classificar_nota(85) == "Aprovado"


def test_deve_retornar_reprovado_para_nota_baixa():
    assert classificar_nota(40) == "Reprovado"


def test_deve_retornar_nota_invalida_para_nota_negativa():
    assert classificar_nota(-5) == "Nota inválida"


# NOVOS TESTES PARA MATAR MUTANTES:

def test_deve_retornar_aprovado_para_nota_100():
    """Testa o limite superior válido (100)"""
    assert classificar_nota(100) == "Aprovado"


def test_deve_retornar_nota_invalida_para_nota_101():
    """Testa logo acima do limite (101)"""
    assert classificar_nota(101) == "Nota inválida"


def test_deve_retornar_reprovado_para_nota_0():
    """Testa o limite inferior válido (0)"""
    assert classificar_nota(0) == "Reprovado"


def test_deve_retornar_nota_invalida_para_nota_negativa_1():
    """Testa logo abaixo do limite (-1)"""
    assert classificar_nota(-1) == "Nota inválida"


def test_deve_retornar_aprovado_para_nota_limite_60():
    """Testa exatamente o limite de aprovação (60)"""
    assert classificar_nota(60) == "Aprovado"


def test_deve_retornar_reprovado_para_nota_limite_59():
    """Testa logo abaixo do limite de aprovação (59)"""
    assert classificar_nota(59) == "Reprovado"
```

## Após Adicionar os Testes

1. Execute os testes para verificar se passam:
```bash
python -m pytest test_classificador.py -v
```

2. Execute mutation testing novamente:
```bash
mutmut run
```

3. Verifique se os mutantes foram mortos:
```bash
mutmut results
```

**Meta**: Nenhum mutante sobrevivente! 🎯

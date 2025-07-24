# Mutation Testing com Mutmut

Este diretório contém um exemplo de **mutation testing** usando a ferramenta `mutmut` para avaliar a qualidade dos testes do classificador de notas.

## O que é Mutation Testing?

Mutation testing é uma técnica que avalia a eficácia dos testes introduzindo pequenas mudanças (mutações) no código e verificando se os testes conseguem detectar essas alterações.

### Resultados Possíveis:
- **🎉 Killed (Morto)**: O teste detectou a mutação - ✅ **Bom!**
- **🙁 Survived (Sobreviveu)**: O teste não detectou a mutação - ❌ **Problema!**
- **🫥 Skipped**: Mutação ignorada
- **⏰ Timeout**: Teste demorou muito para executar
- **🤔 Suspicious**: Resultado suspeito
- **🔇 Error**: Erro durante execução

## Estrutura dos Arquivos

```
mutacao/
├── classificador.py          # Código fonte a ser testado
├── test_classificador.py     # Testes para o classificador
├── setup.cfg                 # Configuração do mutmut
├── README.md                 # Este arquivo
└── EXEMPLO_TESTES.md         # Exemplos de como matar mutantes
```

## Pré-requisitos

Certifique-se de que o ambiente virtual está ativado:

```bash
# Na pasta raiz do projeto
source venv/bin/activate
```

## Como Executar

### 1. Executar Mutation Testing

Na pasta `mutacao/`, execute:

```bash
mutmut run
```

Este comando irá:
- Gerar mutações automaticamente no código
- Executar os testes para cada mutação
- Mostrar resultados em tempo real

### 2. Ver Apenas Mutantes Sobreviventes

```bash
mutmut results
```

Mostra **apenas** os mutantes que **sobreviveram** (não foram detectados pelos testes).

### 3. Ver Todos os Mutantes (Mortos e Vivos)

```bash
mutmut results --all true
```

Mostra **todos** os mutantes com seus status (killed/survived).

### 4. Examinar Mutantes Específicos

Para ver exatamente qual mutação foi feita:

```bash
# Ver um mutante específico
mutmut show classificador.x_classificar_nota__mutmut_1

# Ver quais testes são executados para um mutante
mutmut tests-for-mutant classificador.x_classificar_nota__mutmut_1
```

### 5. Interface Navegável

Para uma visualização mais amigável:

```bash
# Navegador interativo (só mutantes sobreviventes)
mutmut browse

# Navegador mostrando também os mutantes mortos
mutmut browse --show-killed
```

Use as teclas:
- `q`: Sair
- `↑↓`: Navegar
- `Enter`: Ver detalhes do mutante

## Interpretando os Resultados

### Exemplo de Saída Durante Execução:
```
16/16  🎉 16 🫥 0  ⏰ 0  🤔 0  🙁 0  🔇 0
```

- **16/16**: Total de mutações processadas
- **🎉 16**: 16 mutações foram detectadas (mortas)
- **🙁 0**: 0 mutações sobreviveram (não detectadas)

### Score de Qualidade:
**Score = Mortos / Total = 16/16 = 100%** 

## Analisando Mutantes (Exemplo de Processo)

Quando um mutante sobrevive, exemplo do processo que seguimos:

```bash
# 1. Ver mutantes sobreviventes
$ mutmut results
classificador.x_classificar_nota__mutmut_2: survived

# 2. Examinar o mutante
$ mutmut show classificador.x_classificar_nota__mutmut_2
# Output mostra: nota > 100 foi alterado para nota > 101

# 3. Entender o problema
# Não há teste para nota = 101

# 4. Adicionar teste específico
def test_deve_retornar_nota_invalida_para_nota_101():
    assert classificar_nota(101) == "Nota inválida"

# 5. Executar novamente
$ mutmut run
```

## Comandos Úteis para Debugging

### Limpar Cache e Recomeçar
```bash
rm -rf .mutmut-cache
mutmut run
```

## Configuração (setup.cfg)

```ini
[mutmut]
paths_to_mutate=classificador.py
test_command=python -m pytest test_classificador.py -x
runner=python
```

## Testes que Garantem 100% de Qualidade

Nossos testes finais cobrem todos os casos críticos:

```python
def test_deve_retornar_aprovado_para_nota_alta():
    assert classificar_nota(85) == "Aprovado"

def test_deve_retornar_reprovado_para_nota_baixa():
    assert classificar_nota(40) == "Reprovado"

def test_deve_retornar_nota_invalida_para_nota_negativa():
    assert classificar_nota(-5) == "Nota inválida"

def test_deve_retornar_reprovado_para_nota_0():
    """Testa o limite inferior válido (0)"""
    assert classificar_nota(0) == "Reprovado"

def test_deve_retornar_aprovado_para_nota_limite_60():
    """Testa exatamente o limite de aprovação (60)"""
    assert classificar_nota(60) == "Aprovado"

def test_deve_retornar_reprovado_para_nota_limite_59():
    """Testa logo abaixo do limite de aprovação (59)"""
    assert classificar_nota(59) == "Reprovado"

def test_deve_retornar_aprovado_para_nota_100():
    assert classificar_nota(100) == "Aprovado"

def test_deve_retornar_nota_invalida_para_nota_101():
    """Testa exatamente uma nota acima do limite válido"""
    assert classificar_nota(101) == "Nota inválida"

def test_deve_retornar_nota_invalida_para_nota_acima_de_100():
    assert classificar_nota(105) == "Nota inválida"
```

## Workflow Completo Utilizado

```bash
# 1. Instalar mutmut
pip install mutmut

# 2. Configurar setup.cfg
# (arquivo já configurado)

# 3. Executar mutation testing inicial
mutmut run

# 4. Identificar sobreviventes
mutmut results
# Output: 4 mutantes sobreviventes

# 5. Analisar cada sobrevivente
mutmut show classificador.x_classificar_nota__mutmut_4
mutmut show classificador.x_classificar_nota__mutmut_5
mutmut show classificador.x_classificar_nota__mutmut_9
mutmut show classificador.x_classificar_nota__mutmut_10

# 6. Adicionar testes específicos para matar mutantes
# (editamos test_classificador.py)

# 7. Verificar se testes passam
python -m pytest test_classificador.py -v

# 8. Executar mutation testing novamente
mutmut run

# 9. Confirmar 100% de sucesso
mutmut results
# (nenhum output = sucesso!)
```

## Lições Aprendidas

### Mutantes Típicos e Como Matá-los:

1. **`>` → `>=`**: Testar valor exato do limite
2. **`<` → `<=`**: Testar valor exato do limite
3. **`or` → `and`**: Testar casos onde uma condição é verdadeira
4. **Constantes numéricas**: Testar valores adjacentes

### Pontos Críticos para Testar:

- **Valores limite**: 0, 60, 100
- **Valores fora dos limites**: -1, 101
- **Valores adjacentes**: 59, 61
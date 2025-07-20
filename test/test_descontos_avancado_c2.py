from src.sistema_descontos_avancado import calcular_desconto_c2


# Teste 1: Condição A=True, Condição B=False. Resultado da Decisão: False.
def test_condicao_preco_verdadeira_vip_falsa():
    assert calcular_desconto_c2(600, False) == 600


# Teste 2: Condição A=False, Condição B=True. Resultado da Decisão: False.
def test_condicao_preco_falsa_vip_verdadeira():
    assert calcular_desconto_c2(400, True) == 400


# Teste 3: Condição A=True, Condição B=True. Resultado da Decisão: True.
def test_condicao_preco_verdadeira_vip_verdadeira():
    assert calcular_desconto_c2(800, True) == 680


# Teste 4: Condição A=False, Condição B=False. Resultado da Decisão: False.
def test_condicao_preco_falsa_vip_falsa():
    assert calcular_desconto_c2(300, False) == 300

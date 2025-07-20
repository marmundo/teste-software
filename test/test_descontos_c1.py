# arquivo: tests/test_descontos_c1.py
from src.sistema_descontos import calcular_desconto_c1


# Teste para o caminho TRUE da decisão (preco > 100)
def test_caminho_verdadeiro_com_desconto():
    assert calcular_desconto_c1(200) == 180.0


# Teste para o caminho FALSE da decisão (preco <= 100)
def test_caminho_falso_sem_desconto():
    assert calcular_desconto_c1(50) == 50.0

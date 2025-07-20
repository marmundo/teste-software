# arquivo: tests/test_descontos_c0.py


from src.sistema_descontos import calcular_desconto_c0


def test_desconto_aplicado_para_preco_alto():
    """Testa se o desconto é aplicado para um preço alto."""
    assert calcular_desconto_c0(200) == 180.0

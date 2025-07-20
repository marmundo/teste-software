# arquivo: sistema_descontos.py
def calcular_desconto_c0(preco):
    """Aplica um desconto de 10% para preços acima de 100."""
    valor_final = preco
    if preco > 100:
        valor_final = preco * 0.90  # Aplica 10% de desconto
    return valor_final


def calcular_desconto_c1(preco):
    """Aplica um desconto de 10% para preços acima de 100."""
    valor_final = preco
    if preco > 100:  # <-- Ponto de decisão com 2 saídas (True e False)
        valor_final = preco * 0.90
    return valor_final

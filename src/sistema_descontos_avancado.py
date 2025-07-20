def calcular_desconto_c2(preco, eh_vip):
    """Aplica 15% de desconto se o preço for > 500 E o cliente for VIP."""
    valor_final = preco
    # Condição A: preco > 500
    # Condição B: eh_vip
    if preco > 500 and eh_vip:
        valor_final = preco * 0.85
    return valor_final

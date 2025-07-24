# arquivo: classificador.py


def classificar_nota(nota):
    """Classifica uma nota numérica de 0 a 100."""
    if nota > 100 or nota < 0:
        return "Nota inválida"

    if nota >= 60:
        return "Aprovado"
    else:
        return "Reprovado"

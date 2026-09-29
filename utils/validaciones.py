# Revisa que el texto tenga una o más palabras y que solo use letras.
def validar_texto(texto):
    palabras = texto.split()
    if len(palabras) == 0:
        return False
    valido = True
    for palabra in palabras:
        if not palabra.isalpha():
            valido = False
            break
    return valido

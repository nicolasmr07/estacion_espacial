# Función de validación exclusiva del archivo de Rusia. Verifica que un
# texto esté compuesto únicamente por palabras alfabéticas (se usaba para
# validar nombre y destino de una misión). Se conserva exactamente igual.
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

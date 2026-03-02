# BY: Karol Melissa Chacon
# ==========================================================

ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cifrar(texto, llave):
    texto = texto.upper()
    resultado = ""
    for letra in texto:
        if letra in ABECEDARIO:
            posicion = ABECEDARIO.index(letra)
            nueva_posicion = (posicion + llave) % 26
            resultado += ABECEDARIO[nueva_posicion]
        else:
            resultado += letra
    return resultado

def descifrar(texto, llave):
    return cifrar(texto, -llave)

def criptoanalisis_fuerza_bruta(texto):
    resultados = []
    for llave in range(26):
        posible = descifrar(texto, llave)
        resultados.append(f"Llave {llave+1}: {posible}")
    return "\n".join(resultados)

def es_palindromo(texto):

    texto_minuscula = texto.lower()
    texto_sin_espacios = texto_minuscula.replace(" ", "")
    return texto_sin_espacios == texto_sin_espacios[::-1]


print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("palindromo"))  # False
print(es_palindromo("Ella tiro uso mi cabeza como un revolver"))
print(es_palindromo("Alucard"))
print(es_palindromo("miim"))
print(es_palindromo("Mi ama Im"))
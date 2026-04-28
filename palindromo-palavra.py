# Exercício: Verificar se uma palavra é palíndromo
# -----------------------------------------------
# A função deve verificar se essa palavra é um palíndromo.

def palindromo(palavra):
    return palavra == palavra[::-1]


entrada = "121"
print(palindromo(entrada))

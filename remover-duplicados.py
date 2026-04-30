# **Remover duplicados**
# Receba uma lista de números.
# Retorne a lista sem elementos repetidos.

def duplicados(n):
    return sorted(set(n))


numeros = [1, 7, 12, 15, 15, 7, 32, 8, 12]
print(duplicados(numeros))

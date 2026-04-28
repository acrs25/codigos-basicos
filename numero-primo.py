# **Número primo**
# Escreva uma função que recebe um número e retorna se ele é primo ou não

import math


def primo(n):
    if n < 2:
        return f"O número {n} não é primo!"
    elif n == 2:
        return f"O número {n} é primo!"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return f"O número {n} não é primo!"

    return f" O número {n} é primo!"


numero = int(input("Digite um número: "))
print(primo(numero))

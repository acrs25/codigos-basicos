# 📌 Exercícios de lógica e fundamentos
# **Números Pares**
# Imprima todos os números pares de 1 a 100.

def par():
    for i in range(1, 101, 1):
        if i % 2 == 0:
            print(i)


par()

# **Números Ímpares**
# Imprima todos os números ímpares de 1 a 100


def impar():
    for i in range(1, 101, 2):
        print(i)


impar()

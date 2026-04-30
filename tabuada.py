# **Tabuada**
# Receba um número do usuário.
# Mostre a tabuada desse número de 1 a 10

def tabuada(n):
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")


numero = int(input("Digite um número: "))
tabuada(numero)

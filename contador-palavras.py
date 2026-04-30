# **Contador de palavras**
# Receba uma frase.
# Conte quantas palavras existem nela.

def contador(frase):
    lista = len(frase.split())
    return lista


frase = input("Digite uma frase: ")
print(contador(frase))

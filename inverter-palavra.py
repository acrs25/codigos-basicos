# 📌 Manipulação de strings e listas
# **Inverter string**
# Receba uma palavra e mostre ela invertida.
# Exemplo: “Python” → “nohtyP”.

def invertida(palavra_invertida):
    return palavra_invertida[::-1]


palavra = input("Digite uma palavra:")
print(invertida(palavra))

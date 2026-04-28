# Exercício: Verificar palíndromos
# --------------------------------
# Lista de palavras
# Crie uma função que receba uma lista de palavras.
# A função deve verificar se TODAS as palavras da lista são palíndromos.
# Se alguma não for, retorne False. Se todas forem, retorne True.

def palindromo(lista):
    for palavra in lista:
        palavra_invertida = palavra[::-1]
        if palavra_invertida != palavra:
            return False
    return True


palavras = ["434", "ovo", "121"]
print(palindromo(palavras))

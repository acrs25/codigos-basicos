# Frequência de letras
# Receba uma palavra.
# Mostre quantas vezes cada letra aparece (use dicionário)

def frequencia(palavra):
    dicionario = {}
    palavra = palavra.lower()
    for letra in palavra:
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1
    return dicionario


resultado = frequencia("Anne")
print(resultado)

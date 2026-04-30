# 📌 Funções e listas
# **Média de notas**
# Crie uma função que recebe uma lista de notas e retorna a média.

import statistics


def media(notas):
    media_notas = statistics.mean(notas)
    return media_notas


notas_aluno = [4.5, 8.3, 7.5, 9.0]
print(f"{media(notas_aluno):.2f}")

"""
Tarefa de programação: Lista de exercícios - 4

Exercício 1: Lista ordenada
Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro e
devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada.
"""


# Mudar nome da função no envio da terefa para o mesma do exemplo, ordenada().
def sort_list(numbers: list) -> bool:
    ordered_list = sorted(numbers)
    return True if ordered_list == numbers else False

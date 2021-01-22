"""
Tarefa de programação: Lista de exercícios - 6

Exercício 1: Soma dos elementos de uma lista
Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros e
devolve um número inteiro correspondente à soma dos elementos desta lista.

Sua solução deve ser implementada utilizando recursão.
"""


# Mudar nome da função no envio da terefa para o mesma do exemplo, soma_lista().
def sum_list(numbers: list) -> int:
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + sum_list(numbers[1:])

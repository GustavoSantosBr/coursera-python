"""
Tarefa de programação: Lista de exercícios - 5

Exercício 2: Ordenação com bubble sort
Implemente a função bubble_sort(lista), que recebe uma lista com números inteiros como parâmetro e
devolve esta lista ordenada. Utilize o algoritmo bubble sort.

Além de devolver uma lista ordenada, ao longo do processamento sua função deve imprimir o estado atual da
lista toda vez que fizer uma alteração em seus elementos.

Exemplo:

bubble_sort([5, 1, 4, 2])
[1, 5, 4, 2]
[1, 4, 5, 2]
[1, 4, 2, 5]
[1, 2, 4, 5]
# deve devolver [1, 2, 4, 5]
"""


def bubble_sort(numbers: list) -> list:
    for index in range(len(numbers) - 1, 0, -1):
        for range_index in range(index):
            if numbers[range_index] < numbers[range_index + 1]:
                continue
            numbers[range_index], numbers[range_index + 1] = numbers[range_index + 1], numbers[range_index]
            print(numbers)

    return numbers

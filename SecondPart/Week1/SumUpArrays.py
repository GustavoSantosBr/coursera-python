"""
Tarefa de programação: Lista de exercícios - 1

Exercício 2: Soma de matrizes
Escreva a função soma_matrizes(array_x, array_y) que recebe 2 matrizes e devolve uma matriz que represente sua
soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

Exemplos:

array_x = [[1, 2, 3], [4, 5, 6]]
array_y = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(array_x, array_y) => [[3, 5, 7], [9, 11, 13]]

--------------------------------------------------

array_x = [[1], [2], [3]]
array_y = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(array_x, array_y) => False
"""


def dimensions(array_numbers: list) -> tuple:
    return len(array_numbers), len(array_numbers[0])


# Mudar nome da função no envio da terefa para o mesma do exemplo, soma_matrizes().
def sum_arrays(array_x: list, array_y: list):
    dimension_array_x = dimensions(array_x)
    dimension_array_y = dimensions(array_y)

    if dimension_array_x != dimension_array_y:
        return False

    result = []
    lines = len(array_x)
    columns = len(array_x[0])

    for line_index in range(lines):
        result.append([])

        for column_index in range(columns):
            soma = array_x[line_index][column_index] + array_y[line_index][column_index]
            result[line_index].append(soma)
    return result

"""
Tarefa de programação: Lista de exercícios - 1

Exercício 1: Tamanho da matriz
Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as
dimensões da matriz recebida, no formato iXj.

Exemplos:

minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)
3X1

-------------------------------

minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)
2X3
"""


# Mudar nome da função no envio da terefa para o mesma do exemplo, dimensoes().
def dimensions(array_numbers: list):
    print(f"{len(array_numbers)}X{len(array_numbers[0])}")

"""
Tarefa de programação: Lista de exercícios - 4

Exercício 1 - Máximo
Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

Exemplos de execução no shell do Python:

>> maximo(3, 4)
4
>> maximo(0, -1)
0
"""


# Nome da função deve ser igual ao do exemplo.
def maximo(first_number: int, second_number: int) -> int:
    return max(first_number, second_number)

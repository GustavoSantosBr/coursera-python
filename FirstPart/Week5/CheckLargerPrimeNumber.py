"""
Tarefa de programação: Lista de exercícios - 4

Exercício 2 - Primos
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e
devolve o maior número primo menor ou igual ao número passado à função

Exemplos de execução no shell do Python:

>> maior_primo(100)
97
>> maior_primo(7)
7
"""


def check_if_prime_number(number: int) -> bool:
    it_is_divisible = 0

    for index in range(1, number + 1):
        if number % index == 0:
            it_is_divisible += 1

        if it_is_divisible > 2:
            return False
    return True


# Nome da função deve ser igual ao do exemplo.
def maior_primo(number: int) -> int:
    if number < 2:
        return 0

    for index in range(number, 2, -1):
        if check_if_prime_number(index):
            return index


def test_when_number_is_greater_than_two():
    assert maior_primo(100) == 97


def test_when_number_is_less_than_two():
    assert maior_primo(1) == 0

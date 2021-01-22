"""
Tarefa de programação: Lista de exercícios - 6

Exercício 2: Encontrando ímpares em uma lista
Implemente a função encontra_impares(lista), que recebe como parâmetro uma
lista de números inteiros e devolve uma outra lista apenas com os números ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem
"""


# Mudar nome da função no envio da terefa para o mesma do exemplo, encontra_impares().
def find_odd(numbers: list) -> list:
    odd_numbers = []

    if len(numbers) <= 0:
        return numbers

    number = numbers[0]

    if number % 2 > 0:
        odd_numbers.append(number)
    odd_numbers.extend(find_odd(numbers[1:]))

    return sorted(odd_numbers)

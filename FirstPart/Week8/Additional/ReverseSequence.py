"""
Praticar tarefa de programação: Exercícios adicionais (opcionais)

Exercício 2 - Invertendo sequência
Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma
sequência de números inteiros e imprima todos os valores em ordem inversa.
A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.

Exemplo:

Digite um número: 1
Digite um número: 7
Digite um número: 4
Digite um número: 0

4
7
1
"""


def get_data() -> list:
    list_of_numbers = []
    number = None

    while number != 0:
        number = int(input("Digite um número inteiro: "))

        if number == 0:
            break
        list_of_numbers.append(number)

    print()
    return list_of_numbers


def reverse_sequence():
    for number in reversed(get_data()):
        print(number)


reverse_sequence()

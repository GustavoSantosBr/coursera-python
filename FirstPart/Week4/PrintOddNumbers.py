"""
Tarefa de programação: Lista de exercícios - 3

Exercício 2
Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.
Para a saída, siga o formato do exemplo abaixo.

Exemplo:

Digite o valor de n: 5
1
3
5
7
9
"""

number = int(input("Digite um número inteiro e positivo: "))
odd_numbers = []
index = 1

while len(odd_numbers) < number:
    if index % 2 > 0:
        odd_numbers.append(index)
        print(index)
    index += 1

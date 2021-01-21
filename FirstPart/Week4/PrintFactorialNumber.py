"""
Tarefa de programação: Lista de exercícios - 3

Exercício 1
Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.

Exemplo:

Digite o valor de n: 5
120

Dica: lembre-se que o fatorial de 0 vale 1!
"""

number = int(input("Digite um número: "))
factorial_number = 1

for index in range(2, number + 1):
    factorial_number = factorial_number * index

print(f"\n{factorial_number}")

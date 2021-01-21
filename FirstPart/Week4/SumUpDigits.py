"""
Tarefa de programação: Lista de exercícios - 3

Exercício 3
  Escreva um programa que receba um número inteiro na entrada,
  calcule e imprima a soma dos dígitos deste número na saída

Exemplo:

Digite um número inteiro: 123
6
"""

number = input("Digite um número inteiro: ")
summed_number = sum(int(value) for value in number if value.isdigit())

print(f"\n{summed_number}")

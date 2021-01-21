"""
Tarefa de programação: Lista de exercícios - 2

Exercício 1 - Par ou ímpar?
Receba um número inteiro na entrada e imprima

par

quando o número for par ou

ímpar

quando o número for ímpar.
"""

number = int(input("Digite um número inteiro: "))
result = ("Par" if ((number % 2) == 0) else "Ímpar")

print(f"\n{result}")

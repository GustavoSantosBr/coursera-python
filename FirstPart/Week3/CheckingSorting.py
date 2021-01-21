"""
Tarefa de programação: Lista de exercícios - 2

Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente
"""

numbers = []

for index in range(3):
    numbers.append(int(input(f"Digite o {index + 1}º número inteiro: ")))

ordered_numbers = sorted(numbers)
result = "crescente" if numbers == ordered_numbers else "não está em ordem crescente"

print(f"{result}")

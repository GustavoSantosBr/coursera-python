"""
Tarefa de programação: Lista de exercícios - 2

Exercícios 3 - FizzBuzz parcial, parte 2
Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
"""

number = int(input("Digite um número inteiro: "))
result = ("Buzz" if ((number % 5) == 0) else number)

print(f"\n{result}")

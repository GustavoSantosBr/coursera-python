"""
Tarefa de programação: Lista de exercícios - 1

Exercício 2
Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:

Entrada de Dados:
Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7

Saída de Dados:
A média aritmética é 5.5

Dica: uso do print
Quando você usa o comando print para imprimir mais de uma coisa, ele inclui automaticamente espaços entre
os argumentos impressos. Cuidado para não incluir espaços demais na sua resposta! O corretor perceberá
e tirará pontos.

"""

points = [
    float(input("Digite a primeira nota: ")),
    float(input("Digite a segunda nota: ")),
    float(input("Digite a terceira nota: ")),
    float(input("Digite a quarta nota: "))
]
average = sum(points) / len(points)

print(f"A média aritmética é {average}")

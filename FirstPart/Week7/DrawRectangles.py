"""
Tarefa de programação: Lista de exercícios - 5

Exercício 1
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes
à largura e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que
represente o retângulo informado com caracteres '#' na saída.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
##########
##########

-----------------------

digite a largura: 2
digite a altura: 2
##
##
"""


def draw_rectangle(width: int, height: int):
    vertical_line = 1

    while vertical_line <= height:
        horizontal_line = 1

        while horizontal_line <= width:
            print("#", end="")
            horizontal_line += 1

        print("")
        vertical_line += 1


width = int(input("Digite a largura: "))
height = int(input("Digite a altura: "))

draw_rectangle(width, height)

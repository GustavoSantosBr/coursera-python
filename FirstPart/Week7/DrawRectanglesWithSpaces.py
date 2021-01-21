"""
Tarefa de programação: Lista de exercícios - 5

Exercício 2
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não
estiverem na borda do retângulo sejam espaços.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
#        #
##########

---------------------

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
            positions = [horizontal_line, vertical_line]
            print(add_block(positions, width, height), end="")
            horizontal_line += 1

        print("")
        vertical_line += 1


def add_block(positions: list, width: int, height: int) -> str:
    if (positions[1] == 1 or positions[1] == height) or (positions[0] == 1 or positions[0] == width):
        return "#"
    return " "


width = int(input("Digite a largura: "))
height = int(input("Digite a altura: "))

draw_rectangle(width, height)

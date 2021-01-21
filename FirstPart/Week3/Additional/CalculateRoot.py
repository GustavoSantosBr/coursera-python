"""
Praticar tarefa de programação: Exercícios adicionais (opcionais)

Exercício 2 - Desafio da videoaula
Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.

O programa deve receber os parâmetros  A, B, e C da equação  AX^² + BX + c,
respectivamente, e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz real imprima:

a raiz desta equação é X

onde X é o valor da raiz

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente. Exemplos:

as raízes da equação são 1.0 e 2.0

as raízes da equação são -2.0 e 0.0
"""
import math

number = []

for index in range(3):
    number.append(int(input(f"Digite o {index + 1}º número: ")))


def calculate_bhaskara(value_of_a: int, value_of_b: int, value_of_c: int) -> float:
    return (value_of_b ** 2) - (4 * value_of_a * value_of_c)


def check_if_it_has_root() -> str:
    value_of_a = number[0]
    value_of_b = number[1]
    value_of_c = number[2]

    delta = calculate_bhaskara(value_of_a, value_of_b, value_of_c)

    if delta < 0:
        return "esta equação não possui raízes reais"

    roots = [(-value_of_b + math.sqrt(delta)) / (2 * value_of_a), (-value_of_b - math.sqrt(delta)) / (2 * value_of_a)]
    roots = sorted(roots)

    root_of_x = roots[0]
    root_of_y = roots[1]

    if delta > 0:
        return f"as raízes da equação são {root_of_x} e {root_of_y}"

    return f"a raiz desta equação é {root_of_x}"


result = check_if_it_has_root()
print(f"\n{result}")

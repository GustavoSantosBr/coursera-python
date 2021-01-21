"""
Praticar tarefa de programação: Exercícios adicionais (opcionais)

Exercício 2 - Desafio do vídeo "Repetição com while"
Escreva um programa que receba um número inteiro na entrada e verifique se o
número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
Caso exista, imprima "sim"; se não existir, imprima "não".

Exemplos:

Digite um número inteiro: 12345
não

-------------------------------

Digite um número inteiro: 1011
sim
"""


def has_adjacent_number(number: int) -> bool:
    is_equal_number = False
    divided_number = number % 10
    number = number // 10

    while number > 0 and not is_equal_number:
        current_divided_number = number % 10
        number = number // 10

        if current_divided_number == divided_number:
            is_equal_number = True
        divided_number = current_divided_number
    return is_equal_number


number = int(input("Digite um número inteiro: "))
result = "sim" if has_adjacent_number(number) else "não"

print(f"\n{result}")

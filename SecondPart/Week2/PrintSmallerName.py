"""
Tarefa de programação: Lista de exercícios - 2

Exercício 2: Menor nome
Como pedido no primeiro vídeo desta semana, escreva uma função menor_nome(nomes) que recebe uma lista de
strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.

A função deve ignorar espaços antes e depois do nome e deve devolver o menor nome presente na lista.
Este nome deve ser devolvido com a primeira letra maiúscula e seus demais caracteres minúsculos,
independente de como tenha sido apresentado na lista passada para a função.

Quando houver mais de um nome com o menor comprimento dentre os nomes na lista, a função deve devolver
o primeiro nome com o menor comprimento presente na lista.

Exemplos:

menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
# deve devolver 'José'

menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
# deve devolver 'José'

menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
# deve devolver José
"""


# Mudar nome da função no envio da terefa para o mesma do exemplo, menor_nome().
def print_name(names: list) -> str:
    names_size = [len(name.strip()) for name in names]
    smallest_name = ""

    for name in sorted(names):
        name = name.strip()

        if len(name) == min(names_size):
            smallest_name = name

    return smallest_name.capitalize()

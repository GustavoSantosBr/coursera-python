"""
Tarefa de programação: Lista de exercícios - 4

Exercício 2: Busca sequencial
Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e d
evolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de busca sequencial.
Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

Exemplo:

busca(['a', 'e', 'i'], 'e')
# deve devolver => 1

busca([12, 13, 14], 15)
# deve devolver => False
"""


# Mudar nome da função no envio da terefa para o mesma do exemplo, busca().
def sequential_search(elements: list, value):
    for index, element in enumerate(elements):
        if element == value:
            return index

    return False

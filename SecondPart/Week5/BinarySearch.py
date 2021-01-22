"""
Tarefa de programação: Lista de exercícios - 5

Exercício 1: Busca binária
Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e
devolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de busca binária.
Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada
um dos índices testados pelo algoritmo.

Exemplo:

busca(['a', 'e', 'i'], 'e')
1
# deve devolver => 1

busca([1, 2, 3, 4, 5], 6)
2
3
4
# deve devolver => False

busca([1, 2, 3, 4, 5, 6], 4)
2
4
3
# deve devolver => 3
"""


# Mudar nome da função no envio da terefa para o mesma do exemplo, busca().
def binary_search(elements: list, value):
    first = 0
    last = len(elements) - 1

    while first <= last:
        element = (first + last) // 2
        print(element)

        if elements[element] == value:
            return element

        if value < elements[element]:
            last = element - 1
        else:
            first = element + 1

    return False

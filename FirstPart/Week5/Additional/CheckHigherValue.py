"""
Praticar tarefa de programação: Exercícios adicionais (opcionais)

Exercício 2 - Máximo com 3 parâmetros
Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos,
para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

Exemplos de execução no Python Shell

>>maximo(30, 14, 10)
30
>>maximo(0, -1, 1)
1
"""


# Nome da função deve ser igual ao do exemplo.
def maximo(first_number: int, second_number: int, third_number: int) -> int:
    return max(first_number, second_number, third_number)


def test_greater_number_with_positive_numbers():
    assert maximo(1000, 1, 50) == 1000


def test_larger_number_with_negative_numbers():
    assert maximo(-1000, -1, -50) == -1

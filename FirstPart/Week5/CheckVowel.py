"""
Tarefa de programação: Lista de exercícios - 4

Exercício 3 - Vogais
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal
e False se for uma consoante.

Exemplos de execução no shell de Python

>> vogal("a")
True
>> vogal("b")
False
>> vogal("E")
True
"""

VOWELS = ["a", "e", "i", "o", "u"]


# Nome da função deve ser igual ao do exemplo.
def vogal(letter: str):
    return letter.lower() in VOWELS


def test_when_letter_is_vowel():
    assert vogal("A") == True


def test_when_letter_is_not_a_vowel():
    assert vogal("B") == False

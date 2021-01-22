"""
Tarefa de programação: Lista de exercícios - 2

Exercício 1: Letras maiúsculas
Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e
devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.

Para resolver este exercício, pode ser útil verificar uma tabela ASCII, que contém os valores de cada caractere.
Ver https://pt.wikipedia.org/wiki/ASCII

Note que para simplificar a solução do exercício, as frases passadas para a sua função não possuirão caracteres que
não estejam presentes na tabela ASCII apresentada, como ç, á, É, ã, etc.

Dica: Os valores apresentados na tabela são os mesmos devolvidos pela função ord apresentada nas aulas.

Exemplos:

maiusculas('Programamos em python 2?')
# deve devolver 'P'

maiusculas('Programamos em Python 3.')
# deve devolver 'PP'

maiusculas('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'
"""


# Mudar nome da função no envio da terefa para o mesma do exemplo, maiusculas().
def print_uppercase(phrase: str) -> str:
    capital_letters = []

    for index in range(len(phrase)):
        character = phrase[index]
        ascii_code = ord(character)

        if 64 < ascii_code < 91:
            capital_letters.append(character)

    return "".join(capital_letters)

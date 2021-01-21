"""
Praticar tarefa de programação: Exercícios adicionais (opcionais)

Exercício 1 - FizzBuzz
Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

'Fizz' se o número for divisível por 3 e não for divisível por 5;

'Buzz' se o número for divisível por 5 e não for divisível por 3;

'FizzBuzz' se o número for divisível por 3 e por 5;

Caso o número não seja divisível 3 e também não seja divisível por 5,
ela deve devolver o número recebido como parâmetro.

Exemplos de execução no Python Shell

>>fizzbuzz(3)
"Fizz"
>>fizzbuzz(5)
"Buzz"
>>fizzbuzz(15)
"FizzBuzz"
>>fizzbuzz(4)
4

As cadeias de caracteres Fizz e Buzz devem respeitar letras maiúsculas e minúsculas.
"""


def is_divisible_by(number: int, divider: int = 3) -> bool:
    return True if number % divider == 0 else False


# Nome da função deve ser igual ao do exemplo.
def fizzbuzz(number: int):
    is_fizz = is_divisible_by(number)
    is_buzz = is_divisible_by(number, 5)

    if is_fizz and is_buzz:
        return "FizzBuzz"

    if is_fizz:
        return "Fizz"

    if is_buzz:
        return "Buzz"
    return number


def test_when_number_is_fizz_and_buzz():
    assert "FizzBuzz" == fizzbuzz(15)


def test_when_number_is_fizz():
    assert "Fizz" == fizzbuzz(3)


def test_when_number_is_buzz():
    assert "Buzz" == fizzbuzz(5)


def test_when_number_is_neither_fizz_nor_buzz():
    assert 2 == fizzbuzz(2)

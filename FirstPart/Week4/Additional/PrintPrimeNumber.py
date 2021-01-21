"""
Praticar tarefa de programação: Exercícios adicionais (opcionais)

Exercício 1
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Exemplos:

Digite um número inteiro: 13
primo

----------------------------

Digite um número inteiro: 12
não primo
"""


def check_if_prime_number(number: int) -> bool:
    it_is_divisible = 0

    for index in range(1, number + 1):
        if number % index == 0:
            it_is_divisible += 1

        if it_is_divisible > 2:
            return False
    return True


number = int(input("Digite um número inteiro e positivo: "))
result = "primo" if check_if_prime_number(number) else "não primo"

print(f"\n{result}")

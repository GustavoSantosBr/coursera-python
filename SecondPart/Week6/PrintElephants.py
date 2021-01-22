"""
Tarefa de programação: Lista de exercícios - 6

Exercício 3: Elefantes
Este exercício tem duas partes:

Implemente a função incomodam(n) que devolve uma string contendo "incomodam " (a palavra seguida de um espaço) n vezes.
Se n não for um inteiro estritamente positivo, a função deve devolver uma string vazia. Essa função deve ser
implementada utilizando recursão.
Utilizando a função acima, implemente a função elefantes(n) que devolve uma string contendo a letra da música
"Um elefante incomoda muita gente" de 1 até n elefantes.
Se n não for maior que 1, a função deve devolver uma string vazia.
Essa função também deve ser implementada utilizando recursão.
Observe que, para um elefante, você deve escrever por extenso e no singular ("Um elefante...");
para os demais, utilize números e o plural ("2 elefantes...").

Dica: lembre-se que é possível juntar strings com o operador "+". Lembre-se também que é possível transformar
números em strings com a função str().

Dica: Será que neste caso a base da recursão é diferente de  n == 1 n==1?

No exemplo de execução abaixo, note que há uma diferença entre como a string é e como ela é interpretada.
Na função print o símbolo "\n" é interpretado como quebra de linha

>> elefantes(4)
"Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3
elefantes incomodam incomodam incomodam muito mais\n3 elefantes incomodam muita gente\n4 elefantes incomodam incomodam
incomodam incomodam muito mais"
>> print(elefantes(4))
Um elefante incomoda muita gente
2 elefantes incomodam incomodam muito mais
2 elefantes incomodam muita gente
3 elefantes incomodam incomodam incomodam muito mais
3 elefantes incomodam muita gente
4 elefantes incomodam incomodam incomodam incomodam muito mais
>>
"""


# Mudar nome da função no envio da terefa para o mesma do exemplo, incomodam().
def bother(repetitions: int) -> str:
    message = ""

    if repetitions <= 0:
        return message

    message += "incomodam "
    return message + bother(repetitions - 1)


# Mudar nome da função no envio da terefa para o mesma do exemplo, elefantes().
def elephants(repetitions: int, repetition_limit: int or None = None) -> str:
    if not repetition_limit:
        repetition_limit, repetitions = repetitions, 2

    if repetitions > repetition_limit:
        return ""

    end_of_message = f"{repetitions} elefantes {bother(repetitions)}muito mais\n"

    if repetitions < repetition_limit:
        end_of_message += f"{repetitions} elefantes incomodam muita gente\n"

    if repetitions == 2:
        message = "Um elefante incomoda muita gente\n"
        message += end_of_message
        return message + elephants(repetitions + 1, repetition_limit)

    message = end_of_message
    return message + elephants(repetitions + 1, repetition_limit)

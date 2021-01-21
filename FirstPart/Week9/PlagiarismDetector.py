"""
Tarefa de programação: Programa completo - Similaridades entre textos - Caso COH-PIAH
"""

import math
import re

STANDARD_INPUT_VALUE = 1.0


def read_signature() -> list:
    print("\nBem-vindo ao detector automático de COH-PIAH.\nInforme a assinatura típica de um aluno infectado:\n")

    return [float(input("Entre o tamanho médio de palavra: ") or STANDARD_INPUT_VALUE),
            float(input("Entre a relação Type-Token: ") or STANDARD_INPUT_VALUE),
            float(input("Entre a Razão Hapax Legomana: ") or STANDARD_INPUT_VALUE),
            float(input("Entre o tamanho médio de sentença: ") or STANDARD_INPUT_VALUE),
            float(input("Entre a complexidade média da sentença: ") or STANDARD_INPUT_VALUE),
            float(input("Entre o tamanho médio de frase: ") or STANDARD_INPUT_VALUE)]


def read_text() -> list:
    print()
    index = 0
    texts = []
    text = "None"

    while not text == "":
        index += 1
        text = input(f"Digite o {index}º texto (aperte ENTER para sair): ")

        if not text == "":
            texts.append(text.strip())

    return texts


# Mudar nome da função no envio da terefa para o mesma do exemplo, calcula_assinatura.
def calculate_signature(text: str) -> list:
    phrases = []
    words = []

    sentences = separate_sentences(text)

    for value in sentences:
        phrases += separate_phrase(value)

    for phrase in phrases:
        words += separate_words(phrase)

    size_words = len(words)
    size_sentences = len(sentences)
    size_phrases = len(phrases)

    return [
        count_characters(words) / size_words,
        count_different_words(words) / size_words,
        count_unique_words(words) / size_words,
        count_characters(sentences) / size_sentences,
        size_phrases / size_sentences,
        count_characters(phrases) / size_phrases
    ]


# Mudar nome da função no envio da terefa para o mesma do exemplo, compara_assinatura.
def compare_signature(calculated_signature: list, signatures: list) -> float:
    result = 0

    for index in range(0, 6):
        result += math.fabs(calculated_signature[index] - signatures[index])

    result = result / 6
    return round(result, 2)


def separate_sentences(text: str) -> list:
    sentences = re.split(r'[.!?]+', text)

    if sentences[-1] == '':
        del sentences[-1]

    return sentences


def separate_phrase(sentence: str) -> list:
    return re.split(r'[,:;]+', sentence)


def separate_words(phrase: str) -> list:
    return phrase.split()


def count_characters(characters: list) -> int:
    count = 0

    for character in characters:
        count += len(character)

    return count


def count_different_words(words: list) -> int:
    different_words = dict()

    for word in words:
        current_word = word.lower()

        if current_word in different_words:
            different_words[current_word] += 1
        else:
            different_words[current_word] = 1

    return len(different_words)


def count_unique_words(words: list) -> int:
    occurrences = dict()
    unique_words = 0

    for word in words:
        current_word = word.lower()

        if current_word in occurrences:
            if occurrences[current_word] == 1:
                unique_words -= 1
            occurrences[current_word] += 1
        else:
            occurrences[current_word] = 1
            unique_words += 1

    return unique_words


# Mudar nome da função no envio da terefa para o mesma do exemplo, avalia_textos.
def evaluate_texts(texts: list, signatures: list) -> int:
    probabilities = []

    for text in texts:
        calculated_signature = calculate_signature(text)
        compared_signing = compare_signature(calculated_signature, signatures)
        probabilities.append(compared_signing)

    if not probabilities:
        return 0

    lower_probability = min(probabilities)
    lower_probability_index = probabilities.index(lower_probability) + 1

    print(f"\nO autor do texto {lower_probability_index} está infectado com COH-PIAH")
    return lower_probability_index


def main():
    signatures = read_signature()
    evaluate_texts(read_text(), signatures)


main()

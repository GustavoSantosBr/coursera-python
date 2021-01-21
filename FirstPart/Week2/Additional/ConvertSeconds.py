"""
Praticar tarefa de programação: Exercícios adicionais (opcionais)

Exercício 2
Este é o desafio do vídeo "Entrada de Dados".

Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja,
faça um programa em Python que, dada a quantidade de segundos,
"quebre" esse valor em dias, horas, minutos e segundos.
A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato!
Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos.
"""

SECOND_IN_ONE_DAY = 86400  # Segundos em 1 dia
SECOND_IN_AN_HOUR = 3600  # Segundos em 1 hora
SECOND_IN_ONE_MINUTE = 60  # Segundos em 1 minuto

seconds = int(input("Por favor, entre com o número de segundos que deseja converter: "))

hours_left = seconds % SECOND_IN_ONE_DAY
minutes_left = hours_left % SECOND_IN_AN_HOUR

days = seconds // SECOND_IN_ONE_DAY
hours = hours_left // SECOND_IN_AN_HOUR
minutes = minutes_left // SECOND_IN_ONE_MINUTE
seconds = minutes_left % SECOND_IN_ONE_MINUTE

print(f"\n{days} dias, {hours} horas, {minutes} minutos e {seconds} segundos.")

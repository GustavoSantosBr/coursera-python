"""
Tarefa de programação: Programa completo - Jogo do NIM

Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro.
Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um.
Quem tirar as últimas peças possíveis ganha o jogo.

Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1)
peças ao jogador oponente.

Objetivo
Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o
computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada.
Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a
frase "Você começa!"
Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"
Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de
peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de
peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

Seu Programa
Com o objetivo do EP já definido, uma dúvida que deve surgir nesse momento é como modelar o jogo de forma
que possa ser implementado em Python 3 correspondendo rigorosamente às especificações descritas até agora.

Para facilitar seu trabalho e permitir a correção automática do exercício, apresentamos a seguir um modelo,
isto é, uma descrição em linhas gerais de um conjunto de funções que resolve o problema proposto neste EP.
Embora sejam possíveis outras abordagens, é preciso atender exatamente o que está definido abaixo para que
a correção automática do trabalho funcione corretamente.

O programa deve implementar:

Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e
devolve um inteiro correspondente à próxima jogada do computador (ou seja, quantas peças o computador
deve retirar do tabuleiro) de acordo com a estratégia vencedora.
Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua
jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo;
caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e
inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores).
A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente.
A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas
na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a
mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.
Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no
tabuleiro e qual é o máximo de peças a retirar em cada jogada.

Cuidado: o corretor automático não funciona bem se você tiver alguma chamada a input()
antes da definição de todas as funções do jogo (a menos que essa chamada esteja dentro de uma função).
Se seu programa usar input() sem que ele esteja dentro de alguma função, coloque-o no final do programa.

Campeonatos
Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor jogador.
Assim, uma vez que a função partida esteja funcionando, você deverá criar uma outra função chamada campeonato.
Essa nova função deve realizar três partidas seguidas do jogo e, ao final,
mostrar o placar dessas três partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma

Placar: Você ??? X ??? Computador

Execução
Dado que é possível jogar partidas individuais ou campeonatos, seu programa deve começar solicitando ao
usuário que escolha se prefere jogar apenas uma partida (opção 1) ou um campeonato (opção 2).

Atenção: o corretor automático vai verificar se você está utilizando exatamente as mensagens pedidas, como
"Você começa!", "O computador ganhou!" etc. Deixe para usar a sua criatividade em outros lugares!

Veja um exemplo de como deve funcionar o jogo:
"""


def set_up_game():
    game_modes = ["Partida isolada", "Campeonato"]
    game_modes_id = []
    selected_mode_id = 0

    print("\nBem-vindo ao jogo do NIM!\n\nSelecione um modo de jogo para dar início a partida:")

    for index, mode_description in enumerate(game_modes):
        mode_id = index + 1
        game_modes_id.append(mode_id)
        print("({}) - {}".format(mode_id, mode_description.upper()))

    print()

    while selected_mode_id not in game_modes_id:
        selected_mode_id = int(input("Modo de jogo: "))

    print(f"\nVocê selecionou o modo {game_modes[selected_mode_id - 1].upper()}!\n")
    return selected_mode_id


# Nome da função deve ser igual ao do exemplo.
def computador_escolhe_jogada(total_pieces: int, pieces_per_move: int):
    if total_pieces <= pieces_per_move:
        return total_pieces

    for index in range(1, (pieces_per_move + 1)):
        if (total_pieces - index) % (pieces_per_move + 1) == 0:
            return index


# Nome da função deve ser igual ao do exemplo.
def usuario_escolhe_jogada(total_pieces: int, pieces_per_move: int):
    user_move = 0

    if total_pieces >= pieces_per_move:
        move_the_pieces = pieces_per_move
    else:
        move_the_pieces = total_pieces

    while (user_move > move_the_pieces) or user_move < 1:
        user_move = int(input("Quantidade de peças que você vai remover: "))
    return user_move


# Nome da função deve ser igual ao do exemplo.
def partida():
    pieces_per_move = 0
    total_pieces = int(input("Quantidade de peças: "))

    while pieces_per_move < 1:
        pieces_per_move = int(input("Limite de peças por jogada: "))

    user_plays = check_if_the_user_is_the_one_who_starts(total_pieces, pieces_per_move)
    print("\nVOCÊ começa!\n" if user_plays else "\nCOMPUTADOR começa!\n")

    while total_pieces > 0:
        if user_plays:
            removed = usuario_escolhe_jogada(total_pieces, pieces_per_move)
            user_plays = False
            print(f"VOCÊ removeu {removed} peça(s)")
        else:
            removed = computador_escolhe_jogada(total_pieces, pieces_per_move)
            user_plays = True
            print(f"COMPUTADOR removeu {removed} peça(s)")

        total_pieces -= removed
        check_and_print_total_parts(total_pieces)

    if not user_plays:
        print("VOCÊ ganhou!")
        return False

    print("O COMPUTADOR ganhou!")
    return True


def check_and_print_total_parts(total_pieces: int):
    if total_pieces > 1:
        print(f"Agora restam {total_pieces} peças no tabuleiro.\n")
        return

    if total_pieces == 1:
        print("Agora resta apenas uma peça no tabuleiro.\n")


def check_if_the_user_is_the_one_who_starts(total_pieces: int, pieces_per_move: int) -> bool:
    return total_pieces % (pieces_per_move + 1) == 0


# Nome da função deve ser igual ao do exemplo.
def campeonato():
    rounds = 1
    user_score = computer_score = 0

    while rounds < 4:
        print(f"**** Rodada {rounds} ****\n")

        if partida():
            computer_score += 1
        else:
            user_score += 1
        rounds += 1

    print(f"Placar: VOCÊ ({user_score}) X ({computer_score}) COMPUTADOR")


def main():
    game_mode = set_up_game()
    partida() if game_mode == 1 else campeonato()


main()

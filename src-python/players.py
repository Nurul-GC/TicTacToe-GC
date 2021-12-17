from sys import exit

from ai import vitoria, jogada_hm, jogada_pc, jogador_indv


def mostrar_quadro(qd):
    print(f"""
{qd[0]}|{qd[1]}|{qd[2]}
-+-+-
{qd[3]}|{qd[4]}|{qd[5]}
-+-+-
{qd[6]}|{qd[7]}|{qd[8]}
""")


def dois_jogadores(quadro, peca, rodada):
    while True:
        try:
            if ' ' in quadro[:]:
                print(f'\nNivel: 2-Jogadores\nRodada: {rodada}')
                mostrar_quadro(quadro)

                if peca == 'X':
                    jogador_indv(peca, quadro)
                    peca = 'O'
                    if vitoria(quadro):
                        mostrar_quadro(quadro)
                        print(f'\nFim do Jogo..\nVitória para Jogador [{peca}];')
                        exit(0)
                elif peca == 'O':
                    jogador_indv(peca, quadro)
                    peca = 'X'
                    if vitoria(quadro):
                        mostrar_quadro(quadro)
                        print(f'\nFim do Jogo..\nVitória para Jogador [{peca}];')
                        exit(0)
            else:
                rodada -= 1
                print(f'\nSelecione outra Posição de Jogo para [{peca}]!')
        except IndexError:
            rodada -= 1
            print('\nPosição Inválida, Tente Novamente;')
        rodada += 1
        if not vitoria(quadro):
            if ' ' not in quadro[:]:
                print(f'\nFim do Jogo..\nEmpate;')
                mostrar_quadro(quadro)
                exit(0)


def um_jogador(rodada, peca, quadro):
    while True:
        try:
            if ' ' in quadro[:]:
                print(f'\nNível: 1-Jogador\nRodada: {rodada}')
                mostrar_quadro(quadro)

                if peca == 'X':
                    jogada_hm(peca, quadro)
                    peca = 'O'
                    if vitoria(quadro):
                        mostrar_quadro(quadro)
                        print('Fim do jogo..\nVocê Ganhou!')
                        exit(0)
                elif peca == 'O':
                    jogada_pc(peca, quadro)
                    peca = 'X'
                    if vitoria(quadro):
                        mostrar_quadro(quadro)
                        print('Fim do jogo..\nComputador Ganhou!')
                        exit(0)
        except IndexError:
            rodada -= 1
        rodada += 1
        if not vitoria(quadro):
            if ' ' not in quadro[:]:
                mostrar_quadro(quadro)
                print('\nFim do Jogo..\nEmpate;')
                exit(0)

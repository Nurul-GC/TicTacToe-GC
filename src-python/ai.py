from random import randint
from sys import exit


def vitoria(quadro):
    return quadro[0] == quadro[1] and quadro[0] == quadro[2] and quadro[0] != ' ' or \
           quadro[3] == quadro[4] and quadro[3] == quadro[5] and quadro[3] != ' ' or \
           quadro[6] == quadro[7] and quadro[6] == quadro[8] and quadro[6] != ' ' or \
           quadro[0] == quadro[3] and quadro[0] == quadro[6] and quadro[0] != ' ' or \
           quadro[1] == quadro[4] and quadro[1] == quadro[7] and quadro[1] != ' ' or \
           quadro[2] == quadro[5] and quadro[2] == quadro[8] and quadro[2] != ' ' or \
           quadro[0] == quadro[4] and quadro[0] == quadro[8] and quadro[0] != ' ' or \
           quadro[2] == quadro[4] and quadro[2] == quadro[6] and quadro[2] != ' '


def mostrar_quadro(qd):
    print(f"""
{qd[0]}|{qd[1]}|{qd[2]}
-+-+-
{qd[3]}|{qd[4]}|{qd[5]}
-+-+-
{qd[6]}|{qd[7]}|{qd[8]}
""")


def jogada_pc(peca, quadro):
    pc = randint(0, 8)
    if quadro[pc] == ' ':
        quadro[pc] = peca
    else:
        jogada_pc(peca=peca, quadro=quadro)


def jogada_hm(peca, quadro):
    jogada_h = int(input(f'\nSelecione aonde irá Jogar [{peca}]:\n[0-8]> '))
    if quadro[jogada_h] == ' ':
        quadro[jogada_h] = peca
    else:
        print('Selecione outra posição de jogo;')


def jogador_indv(peca, quadro):
    jogada = int(input(f'\nSelecione aonde irá Jogar [{peca}]:\n[0-8]> '))

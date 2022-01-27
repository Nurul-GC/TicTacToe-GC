import platform
from random import randint
from sys import exit


def atualizar():
    limpar_tela = platform.platform()


def vitoria(_quadro):
    return _quadro[0] == _quadro[1] and _quadro[0] == _quadro[2] and _quadro[0] != ' ' or \
           _quadro[3] == _quadro[4] and _quadro[3] == _quadro[5] and _quadro[3] != ' ' or \
           _quadro[6] == _quadro[7] and _quadro[6] == _quadro[8] and _quadro[6] != ' ' or \
           _quadro[0] == _quadro[3] and _quadro[0] == _quadro[6] and _quadro[0] != ' ' or \
           _quadro[1] == _quadro[4] and _quadro[1] == _quadro[7] and _quadro[1] != ' ' or \
           _quadro[2] == _quadro[5] and _quadro[2] == _quadro[8] and _quadro[2] != ' ' or \
           _quadro[0] == _quadro[4] and _quadro[0] == _quadro[8] and _quadro[0] != ' ' or \
           _quadro[2] == _quadro[4] and _quadro[2] == _quadro[6] and _quadro[2] != ' '


def mostrar_quadro(_quadro):
    print(f"""
{_quadro[0]}|{_quadro[1]}|{_quadro[2]}
-+-+-
{_quadro[3]}|{_quadro[4]}|{_quadro[5]}
-+-+-
{_quadro[6]}|{_quadro[7]}|{_quadro[8]}
""")


def jogada_pc(_peca, _quadro):
    pc = randint(0, 8)
    if _quadro[pc] == ' ':
        _quadro[pc] = _peca
    else:
        jogada_pc(_peca=_peca, _quadro=_quadro)


def jogada_hm(_peca, _quadro):
    jogada_h = int(input(f'\nSelecione aonde irá Jogar [{_peca}]:\n[0-8]> '))
    if _quadro[jogada_h] == ' ':
        _quadro[jogada_h] = _peca


def jogador_indv(_peca, _quadro):
    jogada = int(input(f'\nSelecione aonde irá Jogar [{_peca}]:\n[0-8]> '))
    if _quadro[jogada] == ' ':
        _quadro[jogada] = _peca

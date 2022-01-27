#! /usr/bin/python3

# ******************************************************************************
#  Direitos Autorais (c) 2019-2020 Nurul GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

from sys import exit
from ai import vitoria, atualizar
from plays import um_jogador, dois_jogadores

peca = 'X'
rodada = 0
quadro = [' '] * 9

if __name__ == '__main__':
    while not vitoria(quadro):
        jogo = str(input('Selecione o nível: (1)Jogador ou (2)Jogadores ou (S)air..\n> '))
        if jogo == '1':
            atualizar()
            um_jogador(rodada=rodada, peca=peca, quadro=quadro)
        elif jogo == '2':
            atualizar()
            dois_jogadores(rodada=rodada, peca=peca, quadro=quadro)
        elif jogo.lower() == 's':
            exit(0)
        else:
            print('\nDigite 1, 2..\nOu s para sair!')
        if ' ' not in quadro[:]:
            confirma = input("\nPressione (s) para sair...\n> ")
            if confirma == 's':
                exit(0)

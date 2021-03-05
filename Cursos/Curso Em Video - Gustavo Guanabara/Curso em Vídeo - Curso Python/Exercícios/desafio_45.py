# Program: desafio_045.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 19:36

import random

opcoes_computador = ['PEDRA', 'PAPEL', 'TESOURA']
opcao_pessoal = str(input('Digite a sua opção do jogo: '))

opcao_pessoal = opcao_pessoal.upper()
opcao_automatica = random.sample(opcoes_computador, 1)
opcao_automatica = opcao_automatica[0]

if opcao_pessoal in opcoes_computador:
    if opcao_automatica == 'PEDRA' and opcao_pessoal == 'TESOURA':
        print('{} ganha de {}'.format(opcao_automatica, opcao_pessoal))
        print('Computador ganhou!')
    elif opcao_automatica == 'PAPEL' and opcao_pessoal == 'PEDRA':
        print('{} ganha de {}'.format(opcao_automatica, opcao_pessoal))
        print('Computador ganhou!')
    elif opcao_automatica == 'TESOURA' and opcao_pessoal == 'PAPEL':
        print('{} ganha de {}'.format(opcao_automatica, opcao_pessoal))
        print('Computador ganhou!')
    elif opcao_pessoal == 'PEDRA' and opcao_automatica == 'TESOURA':
        print('{} ganha de {}'.format(opcao_pessoal, opcao_automatica))
        print('Jogador ganhou!')
    elif opcao_pessoal == 'PAPEL' and opcao_automatica == 'PEDRA':
        print('{} ganha de {}'.format(opcao_pessoal, opcao_automatica))
        print('Jogador ganhou!')
    elif opcao_pessoal == 'TESOURA' and opcao_automatica == 'PAPEL':
        print('{} ganha de {}'.format(opcao_pessoal, opcao_automatica))
        print('Jogador ganhou!')
    else:
        print('{} = {}'.format(opcao_pessoal, opcao_automatica))
        print('Ninguém ganhou!')
else:
    print('Opção Invalida!')
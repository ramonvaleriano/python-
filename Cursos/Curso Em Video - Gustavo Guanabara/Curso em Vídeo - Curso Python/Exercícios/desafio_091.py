# Program: desafio_091.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 08:42

from random import randint
from random import choice
from operator import itemgetter
import string
import time

jogadores = dict()
ranking = dict()
quant_games = 4
maior = 0
jogador_maior = 0
nomes = string.ascii_uppercase
for q in range(quant_games):
    nome = str(choice(nomes)).upper()
    dado = randint(1, 6)
    jogadores[nome] = dado
    if dado>maior:
        maior = dado
        jogador_maior = nome
for chave, elemento in jogadores.items():
    time.sleep(1)
    print(f'{chave} jogou {elemento}')
print()
time.sleep(1)
print(f'A maior jogada foi: {maior} com o jogador {jogador_maior} ')
print(f'\nA ordem dos jogadores é: \n')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)
for r in ranking:
    print(f'{r[0]} jogou {r[1]}.')


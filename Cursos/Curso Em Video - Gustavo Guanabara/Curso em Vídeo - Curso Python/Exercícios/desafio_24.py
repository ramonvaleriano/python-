# Program: desafio_24.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 09:55

def verifica(n_cidade):
    if n_cidade.upper().startswith('SANTOS'):
        print('O nome da cidade começa com Santos!')
    else:
        print('O nome da cidadenão  Nãocomeça com Santos!')

nome_cidade = str(input('Digite o nome de sua cidade: '))
verifica(nome_cidade)
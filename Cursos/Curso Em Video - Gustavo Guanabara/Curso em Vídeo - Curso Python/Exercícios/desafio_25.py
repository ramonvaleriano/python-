# Program: desafio_25.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 10:01

def verifica(n_pessoa):
    if n_pessoa.upper().count('SILVA'):
        print('O nome {}, contem o sobrenome {}'.format(n_pessoa, "SILVA"))
    else:
        print('Não há o sobrenome Silva')

nome = str(input('Digite o seu nome completo: '))
verifica(nome)
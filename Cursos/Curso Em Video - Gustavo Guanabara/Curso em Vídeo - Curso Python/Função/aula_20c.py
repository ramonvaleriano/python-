# Program: aula_20c.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 11:31

def mostralinha(quantidade):
    print('='*quantidade)

def mensagem(msg, linha):
    quantidade = len(msg)
    linha(quantidade)
    print(f'{msg}')
    linha(quantidade)

mensagem('Aprenda Python', mostralinha)
mensagem('Curso em Video', mostralinha)
mensagem('Ramon R. Valeriano', mostralinha)
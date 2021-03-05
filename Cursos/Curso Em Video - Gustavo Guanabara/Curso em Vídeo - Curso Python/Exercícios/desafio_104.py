# Program: desafio_104.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 08/10/2020 - 16:44

def numerointeiro(mensagem):
    number = input(mensagem)
    while True:
        if number.isdigit():
            resultado = 'Número Inteiro'
            break
        print(f'ERRO! Digite um número inteiro!')
        number = input(mensagem)
    return resultado

final = numerointeiro('Digite um número para validarmos: ')
print(final)
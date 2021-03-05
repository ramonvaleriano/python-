# Program: desafio_097.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 14:11

def mensage(frase, f_linha):
    frase_l = frase()
    tamanho = len(frase_l)
    f_linha(tamanho)
    print(f'{frase_l}')
    f_linha(tamanho)

def linha(v_tamanho):
    print('='*v_tamanho)

def entrada():
    frase = str(input('Digite uma frase para a mensaga: '))
    return frase

mensage(entrada, linha)
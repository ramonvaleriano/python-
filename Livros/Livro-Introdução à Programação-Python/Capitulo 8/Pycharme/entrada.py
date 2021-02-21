# Program: entrada.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 23/09/2020 - 06:34

def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v=int(input(mensagem))
            if v>= minimo and v<=maximo:
                return v
            else:
                print('Digite um valor entre {0} e {1}'.format(minimo, maximo))
        except:
            print('Você deve digitar um número inteiro!')


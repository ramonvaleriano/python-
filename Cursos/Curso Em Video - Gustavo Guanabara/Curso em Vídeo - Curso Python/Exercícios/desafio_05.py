# Programa: desafio_05.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 21:56

numero = 0

def entrada():
    global numero
    numero = float(input('Digite um número qualquer: '))
    return numero

def sucessor(numero):
    numero+=1
    return numero

def antecessor(numero):
    numero-=1
    return numero

digito = entrada()
cima = sucessor(digito)
baixo = antecessor(digito)
print('O seu sucessor é: {:5.2f}'.format(cima))
print('O seu antecessor é: {:5.2f}'.format(baixo))

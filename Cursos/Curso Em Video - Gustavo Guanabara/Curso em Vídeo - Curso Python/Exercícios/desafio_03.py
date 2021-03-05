# Programa: desafio_03.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 19:49

number1 = 0
number2 = 0

def entrada():
    global number1
    global number2
    number1 = float(input("Entre com o primeiro número: "))
    number2 = float(input("Entre com o segundo número: "))

def soma():
    global number1
    global number2
    soma = number1+number2
    return soma

entrada()
valor = soma()
print('A soma dos números: {}'.format(valor))
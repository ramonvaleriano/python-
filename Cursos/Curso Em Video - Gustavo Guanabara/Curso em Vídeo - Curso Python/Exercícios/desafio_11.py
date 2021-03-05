# Programa: desafio_11.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 22:47

def area(numero1, numero2):
    result = numero1*numero2
    return result

def tinta(calculo, num1, num2):
    dado = calculo(num1, num2)
    quantidade = (dado/2)
    return quantidade

comprimento = float(input('Digite o comprimento: '))
altura = float(input('Digite a altura: '))

calculo = area(comprimento,altura)
final = tinta(area, comprimento, altura)
print(calculo)
print(final)
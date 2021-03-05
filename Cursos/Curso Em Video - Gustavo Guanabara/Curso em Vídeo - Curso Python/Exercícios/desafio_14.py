# Programa: desafio_14.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 23/09/2020 - 21:45

def conversor(number):
    Fahrenheit = (1.8*number) + 32
    return Fahrenheit

celsius = float(input('Entre com os graus: '))
print(conversor(celsius))
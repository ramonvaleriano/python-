# Programa: desafio_07.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 22:14

numero1 = 0
numero2 = 0

def entrada():
    global numero1
    global numero2
    numero1 = float(input("Entre com o valor da primeira nota: "))
    numero2 = float(input("Entre com o valor da segunda nota: "))

def media():
    global numero1
    global numero2
    result = (numero1+numero2)/2
    print(result)

entrada()
media()
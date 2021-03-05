# Programa: Algoritmo364_fun5.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/06/2020 - 21:51
# Updated:

def conversao(number):
    import math

    pi = math.pi
    result = (number*180)/pi
    return result

radianos = float(input("Digite o número em radianos: "))

print(conversao(radianos))

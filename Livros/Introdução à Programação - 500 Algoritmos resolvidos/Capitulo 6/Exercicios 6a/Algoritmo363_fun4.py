# Programa: Algoritmo363_fun4.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/06/2020 - 21:43
# Updated:

def conversao(number):
    import math

    result = math.radians(number)
    return result

graus = float(input("Digite os Graus: "))
print(conversao(graus))

# Programa: Algoritmo361_fun3.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/06/2020 - 20:53
# Updated:

def dobro(number):
    result = number*2
    return result

def exibir(number, foper):
    print("{0} X 2 = {1}".format(number, foper(number)))

for e in range(3):
    test = float(input("Digite o número desejado: "))
    exibir(test, dobro)
    

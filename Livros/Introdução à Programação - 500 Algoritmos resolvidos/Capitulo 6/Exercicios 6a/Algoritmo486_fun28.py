# Program: Algoritmo486_fun28.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 10/06/2020 - 20:35
# Updated:

def encontrar(lista, number):
    return(number in lista)

numeros = list()

for e in range(10):
    number = float(input("Entre com %d número: " %(e+1)))
    numeros.append(number)
print()

numero1 = float(input("Entre com um número: "))

print(encontrar(numeros, numero1))

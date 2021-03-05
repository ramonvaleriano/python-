# Program: Algoritmo469_fun11.py
# Author: Ramon R. Valerino
# Description:
# Developed: 08/06/2020 - 10:47 
# Updated:

import random

def fatorial(number):
    fat = 1
    for e in range(number, 0, -1):
        fat*=e
    return fat

def teste(number, funcao):
    if number>=0:
        result = funcao(number)
        print(result)
    else:
        print("Não é possível calcular esse fatorial!")

numero =  random.randint(-10, 10)
print(numero)
teste(numero,fatorial)



    

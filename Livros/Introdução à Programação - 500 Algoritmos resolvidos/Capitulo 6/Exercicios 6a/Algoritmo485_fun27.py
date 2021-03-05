# Program: Algoritmo485_fun27.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 10/06/2020 - 16:43
# Updated:

import string
import random

def repeticao(numeros, string, quantity1, quantity2):
    if(quantity1 == quantity2):
        numeros.sort()
        string.sort()
        for e in string:
            print(e*numeros[cont])
            cont+=1
    else:
        print("Impossível")

numeros = list()
string = list()

for e in range(10):
    number = random.randint(1, 21)
    numeros.append(number)

for e in range(10):
    caracter = random.choice(string.ascii_uppercase)
    string.append(caracter)

quantity1 = len(numeros)
quantity2 = len(string)

repeticao(numeros, string, quantity1, quantity2)

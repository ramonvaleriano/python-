# Program: Algoritmo274_Enq13.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 09:39
# Updated:

import math

cont = 0

while cont<=10:
    number = int(input("Enter with a number: "))
    if number>=0:
        cont+=1
        result = math.sqrt(number)
        print(result)

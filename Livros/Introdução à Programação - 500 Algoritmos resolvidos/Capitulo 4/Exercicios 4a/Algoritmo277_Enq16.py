# Program: Algoritmo277_Enq16.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 10:06
# Updated:

import math

while True:
    number = float(input("Enter with a number: "))
    if number <= 0:
        break
    test = math.sqrt(number)
    print(test)
    if test%1==0.00:
        print("Perfect Square!")
    else:
        print("Imperfect Square!")

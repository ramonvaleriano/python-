# Program: Algoritmo203_para30.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 12:19
# Updated:

quantity = int(input("Enter with the quantity of repetition: "))
if quantity >0:
    for e in range(quantity):
        number = float(input("Enter with the %d° number: " %(e+1)))
        result = number*3
        print(result)
else:
    print("Invalid Option!")

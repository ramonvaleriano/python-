# Program: Algoritmo204_para31.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 12:30
# Updated:

quantity = int(input("Enter with the quantity of repetition: "))
bigger = 0
if quantity >0:
    for e in range(quantity):
        number = float(input("Enter with the %d° number: " %(e+1)))
        if number>=bigger:
            bigger=number
    print(bigger)
else:
    print("Invalid Option!")


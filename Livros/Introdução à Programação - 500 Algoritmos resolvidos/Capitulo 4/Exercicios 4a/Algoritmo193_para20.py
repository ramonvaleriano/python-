# Program: Algoritmo193_para20.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 11:27
# Updated:

quantity = int(input("Enter with the quantity: "))
start = 2
if quantity > 0:
    for e in range(1, quantity+1,):
        result = start*e
        print(result)
else:
    print("Invalided Option!")

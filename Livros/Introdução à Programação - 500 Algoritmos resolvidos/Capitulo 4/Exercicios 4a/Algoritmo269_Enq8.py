# Program: Algoritmo269_Enq8.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 11:33
# Updated:

cont = 0
number = 1
while number%6!=0:
    number = int(input("Enter with %d° number: " %(cont+1)))
    square = number**2
    print(square)
    cont+=1

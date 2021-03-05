# Program: Algoritmo262_Enq1.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 11:05
# Updated:
cont = 1
number = int(input("Enter with a number %d°: " %cont))

while number != -999:
    cont+=1
    triple = number*3
    print(triple)
    number = int(input("Enter with a number %d°: " %cont))
    

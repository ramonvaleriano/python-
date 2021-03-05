# Program: Algoritmo281_Enq20.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 11:53
# Updated:

cont = 0
number = int(input("Enter with the %d° number: " %(cont+1)))
bigger = number

while number!=-999:
    cont+=1
    if number>=bigger:
        bigger = number
    number = int(input("Enter with the %d° number: " %(cont+1)))
print(bigger)

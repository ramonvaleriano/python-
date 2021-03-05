# Program: Algoritmo294_Enq33.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 07:04
# Updated:

number = int(input("Enter with a number: "))
cont = 0
cont_t = 0
while number>=0:
    number-=cont
    cont+=2
    cont_t+=1
print(cont_t)

# Program: Algoritmo289_Enq28.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 18:20
# Updated:

number = 0
cont = 0
cont_t = 0
while number>=0:
    number = int(input("Enter with a number: "))
    if number%3==0:
        cont+=1
    cont_t+=1
conversion = (cont_t*cont)/100
print(conversion)

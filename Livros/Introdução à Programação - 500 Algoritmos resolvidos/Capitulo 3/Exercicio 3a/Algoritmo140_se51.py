# Programa: Algoritmo140_se51.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 16:37
# Updated:

name = input("Enter with your name: ")
value = float(input("Enter with bill amount: "))
name = name.upper()
test = name[0]

if(test=="A")or(test=="D")or(test=="M")or(test=="S"):
    discount = value - ((value*30)/100)
    print(discount)
else:
    print("What a shame!")
    print(value)


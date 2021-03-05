# Program: Algoritmo229_Para56.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 22:18
# Updated:

name = input("Enter with your name: ")
quantity = len(name)

for e in range(quantity):
    if e%2==0:
        print(name[e])
        

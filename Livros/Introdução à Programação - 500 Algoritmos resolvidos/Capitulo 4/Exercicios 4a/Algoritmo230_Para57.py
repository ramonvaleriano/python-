# Program: Algoritmo230_Para57.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 22:21
# Updated:

name = input("Enter with your name: ")
quantity = len(name)

for e in range(quantity-1, -1, -1):
    if e%2!=0:
        print(name[e])
        

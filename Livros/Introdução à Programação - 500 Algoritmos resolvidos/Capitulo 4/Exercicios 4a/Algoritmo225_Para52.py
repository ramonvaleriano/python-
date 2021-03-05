# Program: Algoritmo225_Para52.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 22:00
# Updated:

name = input("Enter with your name: ")
quantity = len(name)
print()

for e in range(quantity):
    #print(name[e])
    for n in range(quantity-1, e-1, -1):
        print(name[n], end=" ")
    print()

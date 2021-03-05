# Program: Algoritmo222_Para49.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 21:43
# Updated:

name = input("Enter with your name: ")
quantity = len(name)
print()
#print(quantity)
for e in range(quantity-1, -1, -1):
    #print(e)
    print(name[e], end=" ")

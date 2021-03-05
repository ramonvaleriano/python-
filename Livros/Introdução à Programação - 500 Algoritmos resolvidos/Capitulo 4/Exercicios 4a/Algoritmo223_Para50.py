# Program: Algoritmo223_Para50.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 21:50
# Updated:

name = input("Enter with your name: ")
quantity = len(name)
print()

for e in range(quantity+1):
    for n in range(e):
        print(name[n], end=" ")
    print()

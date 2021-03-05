# Program: Algoritmo233_Para60.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 22:30
# Updated:

bottom = int(input("Enter with the bottom number: "))
higher = int(input("Enter with the higher number: "))

if bottom >= higher:
    aux = bottom
    bottom = higher
    higher = aux
for e in range(bottom, higher+1):
    print(e)

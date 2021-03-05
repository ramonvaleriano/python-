# Program: Algoritmo231_Para58.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 22:22
# Updated:

current = 15
cont = 0
for e in range(current):
    number = float(input("Enter with the %02d° number: " %(e+1)))
    if number>30:
        cont+=1
print()
print(cont)

# Program: Algoritmo235_Para62.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 22:56
# Updated:


number = float(input("Enter with the 1° number: "))
bigger = number
smaller = number
higher = 10

for e in range(1, higher):
    number = float(input("Enter with the %d° number: " %(e+1)))
    if number>=bigger:
        bigger = number
    if number<=smaller:
        smaller = number
print()
print(bigger)
print(smaller)               

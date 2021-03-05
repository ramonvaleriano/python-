# Program: Algoritmo239_Para66.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/202 - 06:58
# Updated:

number = int(input("Enter with the number: "))

fat = 1
soma = 1
for e in range(1, 10):
    fat*=e
    soma+=((number**e)/fat)
print()
print(soma)
    

# Program: Exercicio6_18.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/04/2020 - 20:47
# Updated:

dicionario = {}

name = input("Enter with your name: ")
quantity = len(name)

for letter in range(quantity):
    test = name[letter]
    dicionario[test] = letter
print(dicionario)

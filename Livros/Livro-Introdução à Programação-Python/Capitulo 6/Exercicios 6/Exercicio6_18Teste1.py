# Program: Exercicio6_18Teste1.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/04/2020 - 20:47
# Updated:

dicionario = {}

name = input("Enter with your name: ")
quantity = len(name)

for number,letter in enumerate(name):
    
    dicionario[letter] = number

print(dicionario)
name ="".join(name)
print(name)

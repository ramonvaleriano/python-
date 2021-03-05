# Program: Algoritmo253_Para0.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/202 - 09:18
# Updated:

for e in range(10):
    name = input("Enter with the word: ")
    name = name.upper()
    cont = 0
    for n in name:
        if n=="A":
            cont+=1
    print(cont)
    print()
        

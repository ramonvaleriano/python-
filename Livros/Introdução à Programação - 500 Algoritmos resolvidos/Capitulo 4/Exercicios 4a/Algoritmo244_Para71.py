# Program: Algoritmo244_Para71.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/202 - 07:38
# Updated:

name = input("Enter with a word: ")
name = name.upper()
cont = 0
new_name = list()
quantity = len(name)
for e in name:
    if e=="A":
        e="X"
    elif e=="E":
        e="Y"
    elif e=="I":
        e="W"
    elif e=="O":
        e="K"
    elif e=="U":
        e="Z"
    new_name+=e

print()
print(new_name)
    
    

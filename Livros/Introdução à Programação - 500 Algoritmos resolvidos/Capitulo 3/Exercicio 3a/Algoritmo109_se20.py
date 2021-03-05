# Program: Algoritmo109_se20.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 24/03/2020 - 17:27
# Updated:

name1 = input("Enter with first name: ")
name2 = input("Enter with second name: ")

if name1 >= name2:
    aux = name1[:]
    name1 = name2[:]
    name2 = aux[:]
print("%s - %s" %(name1, name2))

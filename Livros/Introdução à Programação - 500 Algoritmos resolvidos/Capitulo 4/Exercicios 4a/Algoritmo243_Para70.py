# Program: Algoritmo243_Para70.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/202 - 07:14
# Updated:

name = input("Enter with a word: ")
name = name.lower()
cont = 0
quaantity = len(name)
for e in range(quaantity):
    n=name[e]
    if(n=="a")or(n=="e")or(n=="i")or(n=="o")or(n=="u"):
        cont+=1
print(cont)

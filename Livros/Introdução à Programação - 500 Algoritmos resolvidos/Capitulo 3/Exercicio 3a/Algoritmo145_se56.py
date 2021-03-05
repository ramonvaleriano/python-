# Program: Algoritmo145_se56.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 09:31
# Updated:

name = input("Enter with your name: ")
book = input("Enter with the book name: ")
type_ = input("Enter with type of user: ")

type_ = type_.upper()

if(type_=="PROFESSOR"):
    quantity = 10
elif(type_=="ALUNO"):
    quantity = 3
else:
    quantity = 0

print(name)
print(book)
print(type_)
print(quantity)
    

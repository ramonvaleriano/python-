# Program: Algoritmo246_Para73.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/202 - 08:00
# Updated:

contE=0
contB=0
contR=0
cont_age=0

for e in range(20):
    name = input("Enter with your name: ")
    age = int(input("Enter with your age: "))
    opinion = int(input("Enter with your opinion: 1 - 2 - 3: => "))
    if opinion == 3:
        contE+=1
        cont_age+=age
    elif opinion == 2:
        contB+=1
    elif opinion == 11:
        contR+=1
    
media_age = cont_age/contE
convertion = (100*contB)/20
print()
print(media_age)
print(contR)
print(convertion)

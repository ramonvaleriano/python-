# Program: Algoritmo267_Enq6.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 11:24
# Updated:

cont = 0
word = input("Enter with your profession %d°: " %(cont+1))
word = word.upper()
cont_profession = 0

while word!="FIM":
    cont+=1
    if word == "DENTISTA":
        cont_profession+=1
    word = input("Enter with your profession %d°: " %(cont+1))
    word = word.upper()
print(cont_profession)

# Program: Algoritmo331_Enq70.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 22:34
# Updated:

place = int(input("Enter with place: "))

cont = 1

while cont<=5:
    address = int(input("Enter with your address: "))
    if address < place:
        print("Está a sua esquerda!")
    elif address > place:
        print("Está a sua direita!")
    elif address == place:
        print("Campion!")
        break
    cont+=1
if cont==5 and address != place:
    print("Game Over!")
else:
    print("You Won!")

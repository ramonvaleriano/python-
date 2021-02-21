# Program: Listagem6_7.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 30/03/2020 - 14:14
# Updated:

lista = [0,0,0,0,0]
cont = 0
while cont<len(lista):
    lista[cont] = int(input("Enter with the %d° number: " %(cont+1)))
    cont+=1
while True:
    number = int(input("Enter with a number: "))
    if number == 0:
        break
    elif number>=1 and number<=len(lista):
        desejado = lista[number-1]
        print(desejado)
    else:
        print("Invalid Option!")
print("Final do Programa!")
        

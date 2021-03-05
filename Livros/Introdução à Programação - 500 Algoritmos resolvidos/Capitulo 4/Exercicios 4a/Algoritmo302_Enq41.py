# Program: Algoritmo302_Enq41.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 10:31
# Updated:

cont_ower = 0
bigger = 0
cont_total = 0

while True:
    name_beach = input("Enter with the beach name: ")
    name_beach = name_beach.upper()
    if name_beach == "@":
        break
    owner = input("Enter with the hotel woner: Yes Or No: ")
    owner = owner.upper()
    distance = float(input("Enter with the distance: "))
    if owner == "YES":
        cont_ower+=1
    elif owner == "NO":
        if distance>=10:
            print(name_beach)
    else:
        print("Invalid Option!")

    if bigger<=distance:
        bigger = distance

    cont_total+=1
conversion = (cont_total*cont_ower)/100
print(conversion)
print(bigger)

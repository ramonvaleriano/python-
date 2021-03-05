# Program: Algoritmo338_Enq77.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/04/2020 - 20:10
# Updated:

cont_farm = 0
total = 0

while True:
    q_vaca = 0
    q_touro = 0
    q_boi = 0
    q_bezerro = 0
    cont_herd = 0
    sum_farm = 0
    code_farm = int(input("Ebter with the farm code: "))
    if code_farm <= 0:
        break
    while True:
        code_herd = int(input("Enter with the herd code: "))
        if code_herd <= 0:
            break
        type_herd = int(input("Enter with the type of herd: "))
        quantity = int(input("Enter with the number: "))
        if type_herd == 1:
            print("Vaca!")
            q_vaca+=quantity
            sum_farm+=quantity
            cont_herd+=1
        elif type_herd == 2:
            print("Touro!")
            q_touro+=quantity
            sum_farm+=quantity
            cont_herd+=1
        elif type_herd == 3:
            print("Boi!")
            q_boi+=quantity
            sum_farm+=quantity
            cont_herd+=1
        elif type_herd == 4:
            print("Bezerro!")
            q_bezerro+=quantity
            sum_farm+=quantity
            cont_herd+=1
        else:
            print("Invalid Option!")
    total+=sum_farm
    cont_farm+=1
    print(code_farm)
    print(code_herd)
    print(type_herd)
    print(q_vaca)
    print(q_touro)
    print(q_boi)
    print(q_bezerro)
    print(cont_herd)
print()
print(cont_farm)
print(total)

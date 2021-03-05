# Program: Algoritmo148_se59.py
# Athor: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 10:24
# Updated:

region = int(input("Enter with your region: "))
option = int(input("Enter with your option: "))

if(type(region) is int)and(type(option) is int):
    if region == 1:
        if option == 1:
            tax = 500
        elif option == 2:
            tax = 900
        else:
            tax = 0
    elif region == 2:
        if option == 1:
            tax = 350
        elif option == 2:
            tax = 650
        else:
            tax = 0
    elif region == 3:
        if option == 1:
            tax = 350
        elif option == 2:
            tax = 600
        else:
            tax = 0
    elif region == 4:
        if option == 1:
            tax = 300
        elif option == 2:
            tax = 550
        else:
            tax = 0
    else:
        print("You are wrong!")
        tax = 0
else:
    print("You are asshole!")

print(tax)

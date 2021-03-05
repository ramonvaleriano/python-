# Program: Algoritmo332_Enq71.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 22:43
# Updated:

cont_y = 0
cont_n = 0
cont5 = 0
cont10 = 0
cont20 = 0

while True:
    option = input("Enter with the option: ")
    option = option.upper()
    if option == "F":
        break
    elif option == "Y":
        cont_y+=1
        quantity = int(input("Enter with the quantity: "))
        if quantity > 0 and quantity <= 5:
            cont5+=1
        elif quantity > 5 and quantity <= 10:
            cont10+=1
        elif quantity > 10:
            cont20+=1
        else:
            print("Invalid Option!")
    
    elif option == "N":
        cont_n+=1
    else:
        print("Invalid Option!")
conversion1 = (cont_y*cont5)/100
conversion2 = (cont_y*cont10)/100
conversion3 = (cont_y*cont20)/100
print()
print(cont_y)
print(conversion1)
print(conversion2)
print(conversion3)

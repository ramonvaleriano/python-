# Program: Algoritmo322_Enq60.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 18:39
# Updated:

transaction = int(input("Enter with number of transactions: "))
cont = 0
cont_v = 0
cont_p = 0
sum_p = 0
sum_v = 0


while cont<transaction:
    purchase = float(input("Enter with purchase price: "))
    option =  input("Enter with the form payment: ")
    option = option.upper()
    if (option ==  "V" or option == "P") and purchase > 0:
        if option == "V":
            cont_v+=1
            sum_v+=purchase
            print(purchase)
        elif option == "P":
            cont_p+=1
            portion = purchase/3
            sum_p+=purchase
            print(portion)
        sum_total = sum_v + sum_p
        cont+=1
    else:
        print("Invalid Option!")
print(sum_v)
print(sum_p)
print(sum_total)

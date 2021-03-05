# Program: Algoritmo305_Enq44.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 11:34
# Updated:

balance_total = 0
bigger = 0
balance = 0

while True:
    type_client = int(input("Enter with the client type: "))
    if type_client <= 0:
        break
    previous_balance = float(input("Enter with the precious balance: "))
    bigger = previous_balance
    print("Types of Moviment:")
    print("C - Crédito")
    print("D - Débito")
    print("F -  Fim")
    moviment = input("Enter with the moviment type: ")
    moviment = moviment.upper()
    if moviment == "F":
        break
    elif moviment == "C":
        value = float(input("Value: "))
        balance = previous_balance + value
    elif moviment == "D":
        value = float(input("Value: "))
        balance = previous_balance - value
    else:
        print("Invalid Option!")

    if balance>=bigger:
        bigger = balance
        name_bigger = type_client 
        
    print(balance)
    balance_total+=balance
print()
print(name_bigger)
print(bigger)
print(balance_total)
    

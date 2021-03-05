# Program: Algoritmo327_Enq65.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 21:11
# Updated:

balance = float(input("Enter whit the balance: "))

while True:
    code = int(input("Enter with the code: "))
    if code == 10:
        value = float(input("Enter with the value: "))
        balance-=value
        if balance<0:
            print("Outstanding balance!")
    elif code == 33:
        value = float(input("Enter with the value: "))
        balance+=value
    elif code == 4:
        value = float(input("Enter with the value: "))
        balance-=value
    else:
        print("Invalid Option!")
    print(balance)




# Program: Algoritmo282_Enq21.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 12:01
# Updated:

cont_negative = 0
cont = 0
while True:
    bank_account = int(input("Enter with the banck account number: "))
    if bank_account<0:
        break
    balance = float(input("Enter with your balance: "))
    if balance<0:
        print("Balance Negative!")
        cont_negative+=1
        cont+=1
    elif balance>0:
        print("Balance Positive!")
        cont+=1
    else:
        print("Invalid Balance!")
result = (cont*cont_negative)/100
print(result)

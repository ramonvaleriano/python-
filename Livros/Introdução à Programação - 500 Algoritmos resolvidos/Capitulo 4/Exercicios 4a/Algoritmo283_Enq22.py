# Program: Algoritmo283_Enq22.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 13:13
# Updated: 04/04/2020 - 17:24

balance_total = 0
cont_number = 0
cont = 0
while cont_number <= 10000:
    bank_account = int(input("Enter with the banck account number: "))
    if bank_account == -9999:
        break
    balance = float(input("Enter with your balance: "))
    if balance<0:
        print("Balance Negative!")
        print(balance)
        cont_negative+=1
        cont+=1
    elif balance>0:
        print("Balance Positive!")
        print(balance)
        cont+=1
    else:
        print("Invalid Balance!")
    cont_number+=cont
    balance_total+=balance
print()
print(cont_number)
print(balance_total)

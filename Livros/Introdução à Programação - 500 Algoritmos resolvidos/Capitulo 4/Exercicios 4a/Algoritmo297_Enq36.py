# Program: Algoritmo297_Enq36.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 07:31
# Updated:

daily = 30
tax = 0
total = 0
result = 0

while True:
    name = input("Enter with the client name: ")
    name = name.upper()
    if name == "FIM":
        break
    quantity = int(input("Enter with the number of daily: "))
    if quantity<10:
        tax = 15
    elif quantity>=10:
        tax = 8
    result = (daily+tax)*quantity
    total+=result
    print(name)
    print(quantity)
    print(result)
print()
print(total)
print()

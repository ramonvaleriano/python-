# Program: Algoritmo291_Enq30.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/04/2020 - 08:56
# Updated:

cont = 0

while True:
    request_number = int(input("Enter with the request number: "))
    if request_number == 0:
        break
    print("Enter with the complete date --  ")
    day = int(input("Enter with the day: "))
    month = int(input("Enter with the month: "))
    year = int(input("Enter with the year: "))
    slingle_price = float(input("Enter with the single price: "))
    quantity = int(input("Enter with the quantity: "))
    cont+=1
    result = slingle_price * quantity
    print()
    print(request_number)
    print("%02d/%02d/%d" %(day, month, year))
    print(result)
    print()

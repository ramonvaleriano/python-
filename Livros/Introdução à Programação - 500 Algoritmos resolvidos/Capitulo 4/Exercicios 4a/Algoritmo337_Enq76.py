# Program: Algoritmo337_Enq76.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/04/2020 - 19:50
# Updated:

while True:
    registry = int(input("Enter with the number of the register: "))
    if registry <= 0:
        break
    taxation = float(input("Enter with the taxation: "))
    months = int(input("Enter with the numbers of months: "))
    if taxation > 0 and months > 0:
        if taxation<=500:
            tax = 1
            tax_sum = tax*months
        elif taxation > 500 and taxation <= 1800:
            tax = 2
            tax_sum = tax*months
        elif taxation > 1800 and taxation <= 5000:
            tax = 4
            tax_sum = tax*months
        elif taxation > 5000 and taxation <= 12000:
            tax = 7
            tax_sum = tax*months
        elif taxation > 12000:
            tax = 10
            tax_sum = tax*months
        else:
            print("Invalid Option!")
        result = taxation + ((tax_sum*taxation)/100)  
        print(registry)
        print(taxation)
        print(tax_sum)
        print(result)
    

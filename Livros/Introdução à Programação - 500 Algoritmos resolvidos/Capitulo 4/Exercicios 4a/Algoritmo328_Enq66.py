# Program: Algoritmo328_Enq66.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 21:22
# Updated:

stock = int(input("Enter with the stock: "))
unit_price = float(input("Enter with unit price: "))
minimum = (stock*10)/100
while stock > minimum:
    register = int(input("Enter with register: "))
    if register < 0:
        break
    quantity =  int(input("Enter with the quantity: "))
    conversion = (stock*10)/100
    if quantity <= conversion:
        stock-=quantity
        value =  quantity*unit_price
        print(register)
        print(quantity)
        print(value)
    else:
        print("Failed")
        print(stock)
        
    

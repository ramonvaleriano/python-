# Program: Exercicio3_11.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/03/2020 - 13:05 
# Updated:

value = float(input("Enter with the purchase price: "))
discount = float(input("Enter with the discount: "))

discount_price = (value*discount)/100
new_value = value - discount_price

print("The discount pric is R$%5.2f, and new purchase price %5.2f" %(discount_price, new_value))

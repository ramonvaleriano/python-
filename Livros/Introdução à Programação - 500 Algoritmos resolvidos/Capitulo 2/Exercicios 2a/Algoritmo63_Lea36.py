# Program: Algoritmo63_Lea36.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/03/2020 - 18:50
# Updated:

valor_class = float(input("Enter with the value of the hour class: "))
quantity = int(input("Quantity of the class: "))
discount = float(input("Enter with the discount INSS: "))

value_quantity = valor_class * quantity
new_value = value_quantity - ((value_quantity*discount)/100)

print(new_value)


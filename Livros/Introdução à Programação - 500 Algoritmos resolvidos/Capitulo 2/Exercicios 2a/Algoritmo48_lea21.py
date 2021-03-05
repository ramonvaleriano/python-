# Program: Algoritmo48_lea21.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/03/2020 - 21:05
# Updated:

salary = float(input("Enter with minimum wage: "))
kwh = float(input("Enter with the quantity KWH: "))

value_kwh = (100*salary)/((1/7)*salary)
quantity_kwh = kwh * value_kwh
value = quantity_kwh - ((quantity_kwh*10)/100)

print(quantity_kwh)
print(value_kwh)
print(value)

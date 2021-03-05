# Program: Algoritmo79_leia52.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/03/2020 - 19:00
# Updated:

value = float(input("Enter with the value: "))
rate = float(input("Enter with the rate: "))
month = int(input("Enter with the month: "))

conversion = value*((((1+rate)**month)-1)/rate)

print(convesion)

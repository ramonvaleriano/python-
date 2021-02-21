# Program: Exercicio4_9.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 15:28
# Updated:

house = float(input("The value of the house: "))
salary = float(input("The value of the salary: "))
plots = int(input("The quantity of plots: "))

tax = (salary*30)/100
value = house/plots

if value <= tax:
    print("Acepty!")
else:
    print("Negativy")

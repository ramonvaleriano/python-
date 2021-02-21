# Program: Exercicio3_10.py
# Author: Ramon R. Valeriano
# Descripiton:
# Developed: 23:15 - 11/03/2020
# Updated:

salary = float(input("Enter with the value of the your salary: "))
increase = float(input("Enter with the increase: "))

new_salary = salary + ((salary*increase)/100)

print("Your new salary is R$ %5.2f" %new_salary)


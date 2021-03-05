# Program: Algoritmo98_se9.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/03/2020 - 09:27
# Updated:

salary = float(input("Enter with the your salary: "))
installment = float(input("Enter with the tax: "))

tax = (salary*30)/100

if installment<=tax:
    print("Accept!")
else:
    print("Negate!")

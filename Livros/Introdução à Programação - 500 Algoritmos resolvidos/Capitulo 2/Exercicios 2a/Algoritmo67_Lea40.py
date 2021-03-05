# Program: Algoritmo67_Lea40.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/03/2020 - 21:40
# Updated:

value = float(input("Enter with the value: "))
rate = float(input("Enter with the rate: "))
time = float(input("Enter with the time: "))

installment = value +(value*(rate/100)*time)

print(installment)

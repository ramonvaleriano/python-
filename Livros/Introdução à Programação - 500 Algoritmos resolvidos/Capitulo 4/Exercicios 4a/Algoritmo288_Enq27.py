# Program: Algoritmo288_Enq27.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 18:18
# Updated:
number = 1000
while number>=1000 and number<=9999:
    number = int(input("Enter with a number: "))
    thousandth = int(number/100)
    decimal = int(number%100)
    result1 = thousandth + decimal
    result2 = result1**2
    if result2 == number:
        print(result2)
        print(thousandth)
        print(decimal)
        print(result1)

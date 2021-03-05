# Program: Algoritmo122_se33.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 09:15
# Updated:

number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))
number3 = float(input("Enter with the third number: "))

if(number1 < (number2+number3))and((number2 < (number1+number3))and
    ((number3 < (number2+number1))):
    print("Accept")
else:
    print("Denied!")

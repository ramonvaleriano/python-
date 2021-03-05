# Program: Algoritmo117_se28.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 07:48
# Updated:

number1 = float(input("Enter with first number: "))
number2 = float(input("Enter with second number: "))
number3 = float(input("Enter with third number: "))

if((number1!=number2)and(number1!=number3)and(number2!=number3)):
    bigger = number1
    smaller = number2
    if((number2>number1)and(number2>number3)):
        bigger=number2
        if number1>number3:
            smaller = number3
        else:
            smaller = number1
    if number3<number2:
        smaller = number3
    if((number3>number1)and(number3>number2)):
        bigger = number3
        if number2>number1:
            smaller = number1
        else:
            smaller = number2
print("The higher number: %5.2f\nThe smallest number: %5.2f" %(bigger, smaller))

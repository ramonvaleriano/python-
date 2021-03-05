# Program: Algoritmo123_se34.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 09:22
# Updated:

number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))
number3 = float(input("Enter with the third number: "))

if(number1<(number2+number3))and(number1<(number2+number3))and(number1<(number2+number3)):
    
    #print("This program works so far!")
    if(number1 == number2)and(number1 == number3):
        print("Equilateral triangle!")
    elif(number1 == number2)or(number1 == number3)or(number2 == number3):
        print("Scalene triangle!")
    else:
        print("Isosceles triangle!")
else:
    print("What the fucks is this?")

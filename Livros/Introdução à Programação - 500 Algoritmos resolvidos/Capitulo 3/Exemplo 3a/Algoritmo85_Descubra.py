# Program: Algoritmo85_Descubra.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 17:10
# Updated:

number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))
number3 = float(input("Enter with the third number: "))

if((number1>=number2)and(number1>=number3)):
    bigger = number1
    if number3>=number2:
        smaller = number2
    else:
        smaller = number3
elif(number2 >= number3):
    bigger = number2
    if number3>=number1:
        smaller = number1
    else:
        smaller = number3
else:
    bigger = number3
    if number2 >= number1:
        smaller = number1
    else:
        smaller = number2
print(bigger)
print(smaller)

# Program: Algoritmo287_Enq26.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 18:10
# Updated:

number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))

if number1 <= number2:
    aux = number1
    number1 = number2
    number2 = number1
rest = number1%number2
while resto!=0:
    number1 = number2
    number2 = rest
    rest = number1%number2
print(number2)

# Program: Algoritmo118_se29Solucao1.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 24/03/2020 - 22:20
# Updated:

number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))
number3 = float(input("Enter with the third number: "))

if((number1 != number2)and(number1 != number3)and(number3 != number2)):
    if((number1 > number2)and(number1 > number2)):
        bigger = number1
        if number2 > number3:
            smaller = number3
            average = number2
        else:
            smaller = number2
            average = number3
    elif number2 > number3:
        bigger = number2
        if number1 > number3:
            smaller = number3
            average = number1
        else:
            smaller = number1
            average = number3
    else:
        bigger = number3
        if number1 > number2:
            smaller = number2
            average = number1
        else:
            smaller = number1
            average = number2
print(smaller)
print(average)
print(bigger)

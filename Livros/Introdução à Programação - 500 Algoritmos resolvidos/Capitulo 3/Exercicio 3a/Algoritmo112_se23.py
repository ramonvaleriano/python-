# Program: Algoritmo112_se23.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 24/03/2020 - 17:37
# Updated:

number1 = float(input("Enter with first number: "))
number2 = float(input("Enter with second number: "))

if number1 > number2:
    bigger = number1
    smaller = number2
elif number1 < number2:
    bigger = number2
    smaller = number1
else:
    bigger = number1
    smaller = number2
    print("Numbers Equals")
print(bigger)
print(smaller)
    

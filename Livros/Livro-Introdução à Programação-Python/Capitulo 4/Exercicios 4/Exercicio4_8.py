# Program: Exercicio4_8
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 15:21
# Updated:

number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))
symbol = input("Enter with the symbol: ")

if symbol == "+":
    result = number1 + number2
elif symbol == "-":
    result = number1 - number2
elif symbol == "/":
    result = number1 / number2
elif symbol == "*":
    result = number1 * number2
else:
    print("You are asshole!")
    result = 0
print(result)

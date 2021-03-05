# Program: Algoritmo88_Calculadora.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/03/2020 - 08:15
# Updated:


print("\n")
print("x"+"-"*17+"x")
print("X"+"-"*3+"CALCULADORA"+"-"*3+"x")
print("x"+"-"*17+"x")
print("\n")
number1 = float(input("Ente with the first number: "))
number2 = float(input("Ente with the second number: "))
symbol = input("Enter with the symbol: ")

if symbol == "+":
    result = number1 + number2
elif symbol == "-":
    result = number1 - number2    
elif symbol == "*":
    result = number1 - number2    
elif symbol == "/":
    result = number1 - number2    
else:
    print("You ate asshole!")
    result = 0
print(result)

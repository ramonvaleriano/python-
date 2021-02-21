# Program: Exercicio5_22.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 10:42
# Updated:


while True:
    number1 = float(input("Enter with the first number: "))
    number2 = float(input("Enter with the second number: "))
    option = input("Enter with the option: ")
    option = option.upper()
    if option == "SAIR":
        break
    if option == "+":
        result = number1+number2
    elif option == "-":
        result = number1-number2
    elif option == "*":
        result = number1*number2
    elif option == "/":
        result = number1-number2
    else:
        print("Invalid Option!")
        result = 0
    print(result)
print("Programa encerrado!")

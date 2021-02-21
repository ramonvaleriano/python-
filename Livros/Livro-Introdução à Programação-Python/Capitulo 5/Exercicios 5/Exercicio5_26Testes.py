# Program: Exercicio5_26Testes.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 30/03/2020 - 12:23
# Updated:

number1 = int(input("Entert with the first number: "))
number2 = int(input("Enter with the second number:"))
result = number1
rest = 0
cont = 0
while result>=number2:
    result-=number2
    cont+=1
rest = result
print(cont)
print(rest)

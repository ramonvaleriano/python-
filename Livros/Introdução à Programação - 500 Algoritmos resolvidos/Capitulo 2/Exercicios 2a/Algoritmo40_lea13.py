# Program: Algoritmo40_lea13.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/03/2020 - 20:05
# Updated:

number1 = int(input("Enter with firs number: "))
number2 = int(input("Enter with second number: "))

dividend = int(number1)
divider = int(number2) 
quotient = int(dividend/divider)
rest = dividend % divider

print("The dividend %d" %dividend)
print("The divider %d" %divider)
print("The quotient %d" %quotient)
print("The rest %d" %rest)

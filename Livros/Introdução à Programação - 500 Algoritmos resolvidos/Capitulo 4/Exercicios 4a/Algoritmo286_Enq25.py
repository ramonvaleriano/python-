# Program: Algoritmo286_Enq25.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 18:04
# Updated:

number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))

if number1 <= number2:
    aux = number1
    number1 = number2
    number2 = number1
sum_ = number1
while sum_%number2!=0:
    sum_+=number1
print(sum_)

# Program: Algoritmo207_Para33.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 16:51
# Updated:

number1 = int(input("Enter with the firt number:"))
number2 = int(input("Enter with the second number:"))
sum_ = 0
if number1 >= 0 and number2 > 0:
    for e in range(number2):
        sum_+=number1
    print(sum_)

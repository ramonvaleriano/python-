# Program: Algoritmo215_Para42.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 18:04
# Updated:

number = int(input("Enter with a number: "))

if number > 0 and (type(number) is int):
    for e in range(1, number+1):
        if number%e==0:
            print(e)

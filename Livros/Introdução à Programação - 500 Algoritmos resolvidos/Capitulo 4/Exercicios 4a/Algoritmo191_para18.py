# Program: Algoritmo191_para18.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 11:15
# Updated:

higher = int(input("Enter with higher number: "))
bottom = 0
increment = int(input("Enter with increment number: "))
if higher > 0 and increment > 0:
    for e in range(bottom, higher+1, increment):
        print(e)
else:
    print("You are asshole!")

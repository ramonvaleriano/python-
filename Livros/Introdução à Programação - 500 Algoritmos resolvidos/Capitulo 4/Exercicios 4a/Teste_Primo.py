# Program: Teste_Primo.py
# Author:
# Description:
# Developed:
# Updated:

number = int(input("Enter with a number: "))

cont = 0

for e in range(1, number+1):
    if number%e==0:
        cont+=1
if cont == 2:
    print()
    print(number)

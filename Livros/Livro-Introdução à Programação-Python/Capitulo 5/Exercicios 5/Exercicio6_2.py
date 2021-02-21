# Program: Exercicio6_2.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 10:27
# Updated:

cont = 0
cont2 = 0
l1 = []
l2 = []
while True:
    number1 = int(input("Enter with the %d° number:" %(cont+1)))
    if number1 == 0:
        break
    l1.append(number1)
    cont+=1
while True:
    number2 = int(input("Enter with the %d° number:" %(cont2+1)))
    if number2 == 0:
        break
    l2.append(number2)
    cont2+=1
print()
print()
l3=l1+l2
print(l3)
l1.extend([40])
l2.extend([50])
print(l3)
print(l1)
print(l2)

# Program: Exercicio6_3.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 10:42
# Updated:

cont = 0
cont2 = 0
l1 = []
l2 = []
l3 = []
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
cont = 0
while cont<len(l1):
    cont2 = 0
    while cont2<len(l2):
        if l1[cont]==l2[cont2]:
            number3=l2[cont2]
            l3.append(number3)
        cont2+=1
    cont+=1
print(l3)

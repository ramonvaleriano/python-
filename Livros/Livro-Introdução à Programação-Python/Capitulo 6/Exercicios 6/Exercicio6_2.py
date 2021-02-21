# Program: Exercicio6_2.py
# Author: Ramon R. Valeriano
# Description:  
# Developed: 19/04/2020 - 17:27
# Updated:

l1 = list()
l2 = []
l3 = list()
while True:
    print("The firt List!")
    number1 = float(input("Enter with a number: "))
    if number1 == 0:
        break
    l1.append(number1)

while True:
    print("The second List!")
    number2 = float(input("Enter with a number: "))
    if number2 == 0:
        break
    l2.append(number2)

l3 = l2+l1
print(l3)
    


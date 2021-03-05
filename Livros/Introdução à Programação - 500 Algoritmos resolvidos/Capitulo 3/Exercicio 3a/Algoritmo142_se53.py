# Program: Algoritmo142_se53.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 08:18
# Updated: 

number1 = float(input("Enter with the firt number:"))
number2 = float(input("Enter with the second number:"))
number3 = float(input("Enter with the third number:"))

if(number1!=number2)and(number1!=number3)and(number3!=number2):
    if number1>number2:
        aux1 = number1
        number1 = number2
        number2 = aux1
    if number2 > number3:
        aux2 = number2
        number2 = number3
        number3 = aux2
    if number1 > number3:
        aux3 = number1
        number1 = number3
        number1 = aux3
    print(number1)
    print(number2)
    print(number3)

    sum_ = number1 + number2 + number3

    if(sum_>0)and(sum_<100):
        print("Equipe desclassificada")
else:
    print("Are you OK?!")
    

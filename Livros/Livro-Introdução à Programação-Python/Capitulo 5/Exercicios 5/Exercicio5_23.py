# Program: Exercicio5_23.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 10:52
# Updated:

number = int(input("Enter with a number: "))
number1 = number
while 1<=number:
    aux = 1
    cont = 0
    while 1<=number1:
        result = number % aux
        if result == 0:
            cont+=1
        aux+=1
        number1+=1
    if cont == 2:
        print(number)
    number+=1

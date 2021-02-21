# Program: exercicio8_1.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 15/09/2020 - 21:10

def maior(a, b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return 'Número iguais!'

number2 = float(input(("Enter com um número: ")))
number1 = float(input(("Enter com um número: ")))

print('O maior número é {}'.format(maior(number1, number2)))
# Program: exercicio8_2.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 15/09/2020 - 21:15

def multiplo(a, b):
    return(a%b==0)

number1 = float(input(("Enter com um número: ")))
number2 = float(input(("Enter com um número: ")))

print('O número {} é muliplo de {}? {}'.format(number1, number2, multiplo(number1, number2)))
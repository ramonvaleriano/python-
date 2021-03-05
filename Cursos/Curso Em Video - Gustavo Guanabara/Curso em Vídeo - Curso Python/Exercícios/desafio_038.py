# Program: desafio_038.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 17:58

number1 = float(input('Digite o primeiro número: '))
number2 = float(input('Digite o segundo número: '))

if number1 > number2:
    print('O primeiro valor é maior!')
elif number2 > number1:
    print('O segundo número é maior!')
else:
    print('Os dois número são iguais!')
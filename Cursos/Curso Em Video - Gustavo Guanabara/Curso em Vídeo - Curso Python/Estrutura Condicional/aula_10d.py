# Program: Aula_10d.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 11:08

number1 = float(input('Digite a sua primeira nota: '))
number2 = float(input('Digite a sua segunda nota: '))

if (number1>0 and number2>0)and(number1<=10 and number2<=10):
    media = (number1+number2)/2
    if media>=7:
        print('Aluno aprovado!')
    elif media>=5 and media<7:
        print('Em recuperação!')
    else:
        print('Aluno reprovado!')
else:
    print('Você tem algum tipo de problema mental! ')
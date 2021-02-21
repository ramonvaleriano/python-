# Program: exercicio8_4.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 15/09/2020 - 21:23

def area_triangulo(base, altura):
    result = ((base*altura)/2)
    return result

base = float(input('Digite o valor da base do triangulo: '))
altura = float(input('Digite o valor da altura do triângulo: '))

result = area_triangulo(base, altura)
print('A área do triângulo é: {}'.format(result))


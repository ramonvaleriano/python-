# Program: aula_8a.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 24/09/2020 - 20:23

import math

number = float(input('Digite um número: '))
result = math.sqrt(number)
print('A raiz quadrada do número {} = {:.3f}'.format(number, result))
print('A raiz quadrada do número {} = {:.3f}'.format(number, math.ceil(result)))
print('A raiz quadrada do número {} = {:.3f}'.format(number, math.floor(result)))
print('A raiz quadrada do número {} = {:.3f}'.format(number, math.trunc(result)))
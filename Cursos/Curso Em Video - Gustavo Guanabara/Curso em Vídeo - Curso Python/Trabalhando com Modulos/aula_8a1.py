# Program: aula_8a1.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 24/09/2020 - 20:31

from math import sqrt, floor

number = float(input('Digite um número: '))
result = sqrt(number)
print('A raiz quadrada do número {} = {:.3f}'.format(number, result))
print('A raiz quadrada do número {} = {:.3f}'.format(number, floor(result)))

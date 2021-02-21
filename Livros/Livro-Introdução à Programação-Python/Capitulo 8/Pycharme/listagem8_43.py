# Program: listagen8_43.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 24/09/2020 - 06:32

import types

def testando(a):
    b = type(a)
    if b == int:
        print('int')
    elif b == float:
        print('float')

number = input('Digite algo: ')
testando(number)

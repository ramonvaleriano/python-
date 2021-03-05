# Program: aula_21e.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 08/10/2020 - 08:53

def test(b):
    a = 8 # A variável A se torna local
    b+=4
    c=2
    print(f'O valor da variável a: {a}')
    print(f'O valor da variável b: {b}')
    print(f'O valor da variável c: {c}')


a = 5
test(a)
print(f'A variável "a" fora da função vale: {a}')
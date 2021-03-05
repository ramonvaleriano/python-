# Program: aula_21g.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 08/10/2020 - 11:47

def funcao(b):
    global a
    a = 8
    b+=4
    c = 2
    print(f'A dentro da função: {a}')
    print(f'B dentro da função: {b}')
    print(f'C dentro da função: {c}')


a = 5
print(f'A fora da função: {a}')
funcao(a)
print(f'A fora da função depois de passar a função: {a}')
# Program: desafio_083.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 06/10/2020 - 07:46

expr = str(input('Digite a expressão: '))
pilha = list()

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão estar certa!')
else:
    print('Sua expressão estar errada!')
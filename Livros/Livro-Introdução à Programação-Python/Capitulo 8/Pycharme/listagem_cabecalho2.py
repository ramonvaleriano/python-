# Program: listagem_cabecalho2.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 16/09/2020 - 06:28

A = 5

def muda_e_imprime():
    A=7
    print('\"A\" dentro da função é: %d' %A)

print('\"A\" fora da função é: %d' %A)
muda_e_imprime()
print('\"A\" fora da função é: %d' %A)

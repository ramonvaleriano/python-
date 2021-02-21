# Program: listagem_VariavelGlobal.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 16/09/2020 - 06:33

A = 5

def muda_e_imprime():
    global A
    A=7
    print('\"A\" dentro da função é: %d' %A)

print('\"A\" fora da função é: %d' %A)
muda_e_imprime()
print('\"A\" fora da função é: %d' %A)

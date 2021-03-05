# Program: aula_14d.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 08:02

n = 1
par = impar = 0
while n!=0:
    n = int(input('Digite um número: '))
    if n!=0:
        if n%2==0:
            par+=1
        else:
            impar+=1
print('Número paras {}\nNúmero impares {}'.format(par, impar))
print('\nAcabou:')
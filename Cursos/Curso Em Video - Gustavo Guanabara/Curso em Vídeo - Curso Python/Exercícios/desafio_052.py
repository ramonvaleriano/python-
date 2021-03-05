# Program: desafio_052.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 28/09/2020 - 20:51

number = int(input('Digite um número qualquer: '))

cont = 0
s = 1
while s<=number:
    if number%s==0:
        cont+=1
    s+=1

if cont == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')
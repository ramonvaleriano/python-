# Program: desafio_050.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 23:17

soma = 0
for e in range(6):
    number = int(input('Digite um número: '))
    if number%2==0:
        soma+=number
print(soma)
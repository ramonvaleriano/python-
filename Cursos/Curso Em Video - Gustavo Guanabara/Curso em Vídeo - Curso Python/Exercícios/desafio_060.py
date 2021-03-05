# Program: desafio_060.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 14:37

number = int(input('Digite o seu númermo: '))
fatorial = 1
f = 1
while number>=f:
    fatorial*=number
    number-=1
print(fatorial)
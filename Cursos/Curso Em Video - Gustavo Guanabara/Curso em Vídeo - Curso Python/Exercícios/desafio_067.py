# Program: desafio_067.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 17:52

while True:
    number = int(input('Digite um número: '))
    if number<0:
        break
    n = 0
    print('='*30)
    for i in range(1, 11):
        n = i * number
        print(f'{i:2} * {number:2} = {n:3}')
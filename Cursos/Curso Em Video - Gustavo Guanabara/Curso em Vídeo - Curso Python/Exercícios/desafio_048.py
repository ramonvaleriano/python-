# Program: desafio_048.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 23:08

soma = 0
for i in range(1, 501):
    if (i%2!=0)and(i%3==0):
        print(i)
        soma+=i
print(soma)


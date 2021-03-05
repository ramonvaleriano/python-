# Program: desafio_054.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 28/09/2020 - 21:15

cont = 0
cont_n = 0
for e in range(7):
    age = int(input('Digite a idade da %d° pessoa: ' %(e+1)))
    if age>=18:
        cont+=1
    else:
        cont_n+=1
print(cont)
print(cont_n)
# Program: exercicio9_4.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 12:37

impares = open("impares.txt", "w")
pares = open("pares.txt", "w")

for number  in range(1, 101):
    if number%2 == 0:
        pares.write(f'{number}\n')
    else:
        impares.write(f'{number}\n')
impares.close()
pares.close()

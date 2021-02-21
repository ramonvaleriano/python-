# Program: Listagem6_5for1.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 30/03/2020 - 13:44
# Updated:

notas = [6,7,5,8,9]
quantity = len(notas)
sum_ = 0
cont = 0
for e in range(quantity):
    print(notas[e])
    sum_+=notas[e]
    cont+=1
print()
media=sum_/cont
print(media)

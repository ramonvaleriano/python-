# Program: Listagem6_5.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 30/03/2020 - 13:44
# Updated:

notas = [6,7,5,8,9]
cont = 0
sum_ = 0
quantity = len(notas)
while cont<quantity:
    #print(cont)
    sum_+=notas[cont]
    print(notas[cont])
    cont+=1
print()
media1 = sum_/quantity
media2 = sum_/cont
print(media1)
print(media2)

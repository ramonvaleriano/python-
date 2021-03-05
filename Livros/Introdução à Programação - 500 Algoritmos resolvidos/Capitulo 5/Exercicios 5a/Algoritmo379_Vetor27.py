# Program: Algoritmo379_Vetor27.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/05/2020 - 20:49 
# Updated:

quantity = 100
lista = list()
cont30 = 0
sum_ = 0
cont_iquals = 0
cont_media = 0
for e in range(quantity):
    number = float(input("Enter with %d° number: " %(e+1)))
    if number == 30:
        cont30+=1
    lista.append(number)
    sum_+=number
media = sum_/quantity
for n in lista:
    if n>media:
        cont_media+=1
    if n==media:
        cont_iquals+=1
print()
print(cont30)
print(cont_media)
print(cont_iquals)
print()

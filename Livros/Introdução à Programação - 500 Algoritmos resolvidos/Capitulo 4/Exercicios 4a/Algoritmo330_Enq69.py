# Program: Algoritmo330_Enq69.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 22:08
# Updated:

sum_income = 0
sum_children = 0
cont_family = 0
higher = 0

while True:
    family_income = float(input("Enter with the family income: "))
    if family_income <= 0 :
        break
    children = int(input("Enter with the number of children: "))
    sum_income+=family_income
    sum_children+=children
    cont_family+=1
    if family_income >= 100:
        higher+=1
media_income = sum_income/cont_family
media_children = sum_children/cont_family
conversion = (higher*cont_family)/100
print(media_income)
print(media_children)
print(conversion)

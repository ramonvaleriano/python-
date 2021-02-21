# Program: Exercicio6_13.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 07:35
# Updated:

T = [-10, -8, 0, 1, 2, 5, -2, -4]
bigger = T[0]
smaller = T[0]
sum_ = 0
cont = len(T)
for e in T:
    if e>=bigger:
        bigger=e
    if e<=smaller:
        smaller = e
    sum_+=e
media = sum_/cont
print(bigger)
print(smaller)
print(media)

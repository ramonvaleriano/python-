# Program: Exercicio6_13.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 21/04/2020 - 12:13
# Updated:

l=[-10, -8, 0, 1, 2, 5, -2, -4]
maximum = l[0]
minimum = l[0]
sum_ = 0
for e in l:
    if e>maximum:
        maximum=e
    if e<minimum:
        minimum=e
    sum_+=e
media = sum_/(len(l))
print(maximum)
print(minimum)
print(media)

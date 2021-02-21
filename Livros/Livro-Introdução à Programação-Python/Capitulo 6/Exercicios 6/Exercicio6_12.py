# Program: Exercicio6_12.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 21/04/2020 - 12:11
# Updated:

l=[1, 7, 2, 4]
maximum = l[0]
minimum = l[0]

for e in l:
    if e>maximum:
        maximum=e
    if e<minimum:
        minimum=e
print(maximum)
print(minimum)

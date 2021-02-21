# Program: Listagem6_34.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 21/04/2020 - 12:17
# Updated:

l = [9,8,7,12,0,13,21]
even = []
odd = list()

for e in l:
    if e%2==0:
        even.append(e)
    else:
        odd.append(e)
print(even)
print(odd)

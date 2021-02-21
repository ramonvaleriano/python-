# Program: Listagem6_34.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 07:42
# Updated:

v = [9,8,7,12,0,13,21]
even = []
odd = []

for e in v:
    if e%2==0:
        even.append(e)
    else:
        odd.append(e)
print(even, end=" ")
print("\n\n")
print(odd, end=" ")

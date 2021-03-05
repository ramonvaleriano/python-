# Program: aula_17d.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 02/10/2020 - 19:24

a = [2, 3, 4, 7]
b = a
print(a)
print(b)
b[2] = 89
print(a)
print(b)
a = [2, 3, 4, 7] 
b = a[:]
b[2] = 89
print(a)
print(b)

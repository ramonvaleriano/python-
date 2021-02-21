# Program: Listagem6_32Tests.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 20/04/2020 - 22:14
# Updated:

l = [5, 7, 9]

for x, e in enumerate(l):
    print("%d - %d" %(x, e))

print("\n\n")

for z in enumerate(l):
    x, e = z
    print("%d - %d" %(x, e))

print(z)

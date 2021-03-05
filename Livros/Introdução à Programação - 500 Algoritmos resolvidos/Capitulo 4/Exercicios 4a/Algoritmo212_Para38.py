# Program: Algoritmo212_Para38.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 17:47
# Updated:

sum_ = 0
for e in range(20):
    number = float(input("Enter with th %d muberm: " %(e+1)))
    result = number**2
    if result < 225:
        sum_+=number
print(sum_)

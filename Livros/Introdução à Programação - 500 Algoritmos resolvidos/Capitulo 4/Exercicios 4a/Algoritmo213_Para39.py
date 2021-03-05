# Program: Algoritmo213_Para49.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 17:53
# Updated:

sum_ = 0
media = 0
current = 12
for e in range(current):
    number = float(input("Enter with the %d number: " %(e+1)))
    sum_+=number
media=sum_/current
print(media)

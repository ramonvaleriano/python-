# Program: Algoritmo196_para23.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 11:53
# Updated:

number = int(input("Enter with a number: "))
sum_ = 0

for e in range(1, number):
    if e%5==0:
        sum_+=e
print(sum_)

# Program: Algoritmo197_para24.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 11:56
# Updated:

quantity =  int(input("Enter with the quantity of odd numbers: "))
sum_=0
start = 1
for e in range(start, (quantity)*2, 2):
    print(e, end=" ")
    sum_+=e
print("\n", sum_)

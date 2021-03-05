# Program: Algoritmo238_Para65.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 23:08
# Updated:

number = int(input("Enter with the number: "))
sum_ = 0
n = number
for e in range(1, number+1):
    sum_+=(e/n)
    n-=1
print("\n", sum_)

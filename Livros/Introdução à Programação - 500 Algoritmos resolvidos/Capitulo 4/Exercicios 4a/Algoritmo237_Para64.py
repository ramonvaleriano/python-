# Program: Algoritmo237_Para64.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 23:04
# Updated:

number = int(input("Enter with the number: "))
sum_ = 1

for e in range(2, number+1):
    if number%2==0:
        sum_-=(1/number)
    else:
        sum_+=(1/number)
print("\n", sum_)

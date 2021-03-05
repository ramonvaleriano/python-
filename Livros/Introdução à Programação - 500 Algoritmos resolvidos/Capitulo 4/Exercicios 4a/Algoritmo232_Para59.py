# Program: Algoritmo232_Para59.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 22:26
# Updated:

current = 20
cont = 0
sum_ = 0
for e in range(current):
    number = float(input("Enter with the %02d° number: " %(e+1)))
    if number>=0:
        sum_+=number
    else:
        cont+=1
print()
print(sum_)
print(cont)

# Program: Algoritmo47_lea20.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/03/2020 - 20:59
# Updated:

number = int(input("Enter with a number: "))

c = int(number/100)
d = int((number%100)/10)
u = number%10

print(c)
print(d)
print(u)

c_new = u*100
d_new = d*10
number_new = c_new + d_new + c
print(number_new)

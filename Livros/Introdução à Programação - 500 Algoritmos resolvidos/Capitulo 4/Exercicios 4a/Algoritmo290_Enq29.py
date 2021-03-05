# Program: Algoritmo290_Enq29.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 18:24
# Updated:

product = 1
sum_ = 0

while True:
    number = int(input("Enter with a number: "))
    if number<0:
        break
    elif number%2==0:
        sum_+=number
    else:
        product*=number
print(sum_)
print(product)

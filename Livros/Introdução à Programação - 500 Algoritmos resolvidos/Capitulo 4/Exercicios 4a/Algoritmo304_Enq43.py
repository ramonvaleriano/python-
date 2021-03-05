# Program: Algoritmo304_Enq43.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 11:23
# Updated:

cont = 0
number = int(input("Enter with the %d° number: " %(cont+1)))
smaller = 0
bigger = 0
cont_total = 0
sum_ = 0
while number != -1:
    cont+=1
    if number >= 100 and number <= 1000:
        sum_+=number
        if number<=smaller:
            smaller = number
    number = int(input("Enter with the %d° number: " %(cont+1)))
media = sum_/cont
print(sum_)
print(media)
    

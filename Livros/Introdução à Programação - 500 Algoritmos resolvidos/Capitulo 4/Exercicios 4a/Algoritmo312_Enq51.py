# Program: Algoritmo312_Enq51.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 07/04/2020 - 10:25
# Updated:

number = int(input("Enter with the integer: "))
multiple8 = 0
cont = 0
sum_ = 0
while number!=-1:
    cont+=1
    if number%8==0:
        multiple8+=1
    sum_+=number
    print(number)
    print()
    number = int(input("Enter with the integer: "))
media = sum_/cont
print()
print(media)
print(multiple8)
print()

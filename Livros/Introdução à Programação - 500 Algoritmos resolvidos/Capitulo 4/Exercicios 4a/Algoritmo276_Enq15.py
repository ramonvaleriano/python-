# Program: Algoritmo276_Enq15.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 10:01
# Updated:

age = int(input("Enter with the your age: "))
cont21 = 0
cont50 = 0
while age>0:
    if age<=21:
        cont21+=1
    elif age>=50:
        cont50+=1
    age = int(input("Enter with the your age: "))
print(cont21)
print(cont50)

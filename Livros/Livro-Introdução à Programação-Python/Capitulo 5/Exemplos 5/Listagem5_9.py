# Program: Listagem5_9.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 29/03/2020 - 11:42
# Update:

number = int(input("Enter with a number: "))
cont = 1

while cont<=10:
    sum_ = cont+number
    print("%03d + %03d = %03d"%(cont, number, sum_))
    cont+=1



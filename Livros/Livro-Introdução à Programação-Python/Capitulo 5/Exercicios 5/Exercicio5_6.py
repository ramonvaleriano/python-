# Program: Exercicio5_6.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 29/03/2020 - 11:46
# Update:

number = int(input("Enter with a number: "))
cont = 0

while cont<=10:
    result = cont*number
    print("%03d + %03d = %03d"%(cont, number, result))
    cont+=1


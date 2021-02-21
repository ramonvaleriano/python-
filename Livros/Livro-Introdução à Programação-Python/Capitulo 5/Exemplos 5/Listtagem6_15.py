# Program: Listtagem6_15.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 08:29
# Updated:

l = []
while True:
    number = int(input("Enter with a number: "))
    if number == 0:
        break
    l.append(number)
cont = 0
while cont<len(l):
    print(l[cont])
    cont+=1
    

# Program: Algoritmo349_SomaVetores.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 11:52
# Updated:

list1 = []
list2 = []
list3 = list()

quantity = 5
print("Enter with number of the first list:")
for e in range(quantity):
    number = float(input(("Enter with %d° number: " %(e+1))))
    list1.append(number)
print()
print("Enter with number of the second list:")
for g in range(quantity):
    number = float(input(("Enter with %d° number: " %(g+1))))
    list2.append(number)
for y in range(quantity):
        test = list1[y]+list2[y]
        list3.append(test)
print("The thrid list: ")
for h in list3:
    print(h)
        

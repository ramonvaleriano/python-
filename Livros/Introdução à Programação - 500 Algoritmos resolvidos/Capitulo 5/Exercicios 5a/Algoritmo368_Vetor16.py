# Program: Algoritmo368_Vetor16.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/04/2020 - 21:15
# Updated:

list1 = list()
list2 = list()
list3 = list()
list4 = list()
quantity = 3

for e in range(quantity):
    number1 = float(input("Enter with the %d° number 1: " %(e+1)))
    list1.append(number1)
    number2 = float(input("Enter with the %d° number 2: " %(e+1)))
    list2.append(number2)
print("\n\n")
for n in range(quantity):
    sum_ = list1[n] + list2[n]
    print("%5.2f + %5.2f = %5.2f" %(sum_, list1[n], list2[n]))
    subtration = list1[n] - list2[n]
    print("%5.2f - %5.2f = %5.2f" %(subtration, list1[n], list2[n]))
    multiplication = list1[n] * list2[n]
    print("%5.2f / %5.2f = %5.2f" %(multiplication, list1[n], list2[n]))
    if list2[n]>0:
        division = list1[n] / list2[n]
        print("%5.2f / %5.2f = %5.2f" %(division, list1[n], list2[n]))
    else:
        print("Invalid Option!")
        division = 0
print("\n\n")
for g in range(quantity):
    number = float(input("Enter with %d° number: " %(g+1)))
    list3.append(number)
list4 = list3[:]
print(list4)

# Program: Algoritmo367_Vetor15.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/04/2020 - 12:08
# Updated:

list1 = list()
quantity = 5
even = 0
sum_ = 0
for e in range(quantity):
    number = int(input("Enter with %d number: " %(e+1)))
    if e == 0 :
        bigger = number
        smaller = number
    if bigger < number:
        bigger = number
    if smaller > number:
        smaller = number
    if number%2 == 0:
        even+=1
    sum_+=number
media = sum_/quantity
converstion = (quantity*even)/100
print("Higher number: ", bigger)
print("Smalled number: ", smaller)
print("The media: ", media)
print("Percentage of even numbers: ", converstion)
quantity = 5
for n in range(quantity):
    for y in range((n+1), quantity):
        if list1[n]>list1[y]:
            aux = list1[n]
            list1[n] = list1[y]
            list1[y] = aux
print("\n\n")
print(list1)

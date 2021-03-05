# Program: Algoritmo216_Para43.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 18:07
# Updated:

even = 0
odd = 0
wrong = 0
for e in range(200):
    number = int(input("Enter with a number: "))
    if(type(number) is int)and(number%2==0):
        even+=1
    elif(type(number) is int)and(number%2!=0):
        odd+=1
    else:
        wrong+=1
print(even)
print(odd)
print(wrong)

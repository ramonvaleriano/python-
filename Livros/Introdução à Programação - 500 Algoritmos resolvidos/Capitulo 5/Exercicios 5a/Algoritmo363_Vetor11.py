# Program: Algoritmo363_Vetor11.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 20:33
# Updated:

list_ = list()
quantity = 10

for e in range(quantity):
    number = int(input("Enter with %d° number: " %(e+1)))
    if number < 0:
        break
    list_.append(number)
for n in list_:
    result = 1/n
    print("%5.2f" %result, end=" ")

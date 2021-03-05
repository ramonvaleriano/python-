# Program: Algoritmo364_Vetor12.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 20:41
# Updated:

list_ = list()
quantity = 10

for e in range(quantity):
    number = int(input("Enter with %d° number: " %(e+1)))
    if number < 0:
        break
    list_.append(number)
print()
for n in list_:
    product = 1
    for g in range(n, 0, -1):
        product*=g
    print("%10.2f" %product, end=" ")

    

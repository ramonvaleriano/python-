# Program: Algortimo377_Vetor25.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/05/2020 - 22:43
# Updated:

quantity = 5
lista = list()
cont = 0
test = 0
for e in range(quantity):
    number =  int(input("Enter with %d° number: " %(e+1)))
    if number == 0:
        break
    
    test = len(lista)
    if test>1:
        last = lista[-1]
        if number == last:
            cont+=1
    else:
        last = 0
    lista.append(number)
print(cont)

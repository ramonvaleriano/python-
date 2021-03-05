# Program: Algoritmo381_Vetor29.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/05/2020 - 21:02
# Updated:

agenda = list()
quantity = 10

for e in range(quantity):
    name = str(input("Enter with the %d° name: " %(e+1)))
    agenda.append(name)
cont = 0
while (cont<(len(agenda))):
    cont2 = 0
    while (cont2<(len(agenda))):
        if agenda[cont]<agenda[cont2]:
            aux = agenda[cont]
            agenda[cont] = agenda[cont2]
            agenda[cont2] = aux
        cont2+=1
    cont+=1
for i, v in enumerate(agenda):
    print("%2d - %-12s" %(i, v))

        


# Program: Exercicio6_1for.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 30/03/2020 - 14:01
# Updated:

notas = [0,0,0,0,0,0,0]
sum_ = 0
cont = 0

for e in notas:
    notas[cont] = float(input("Enter with the %d° note: " %(cont+1)))
    cont+=1
for e in notas:
    print(e)

#while cont<len(notas):
    #notas[cont] = float(input("Enter with the %d° note: " %(cont+1)))
    #sum_+=notas[cont]
    #cont+=1
#print()
#media=sum_/cont
#print(media)
#cont = 0
#while cont<len(notas):
    #print(notas[cont])
    #cont+=1

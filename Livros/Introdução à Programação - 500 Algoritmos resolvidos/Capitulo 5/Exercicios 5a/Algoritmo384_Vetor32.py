# Program: Algoritmo384_Vetor32.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/05/2020 - 21:57
# Updated:

total_candidatos = []
quantity_total = 5
quantity = 3
for e in range(quantity_total):
    candidato = list()
    sum_= 0
    name = str(input("Enter with the name: "))
    name = name.upper()
    candidato.append(name)
    for n in range(quantity):
        note = float(input("%d° note: " %(n+1)))
        if note>0:
            if n == 0:
                conversion = note*2
                candidato.append(conversion)
            elif n == 1:
                conversion = note*3
                candidato.append(conversion)
            elif n == 2:
                conversion = note*5
                candidato.append(conversion)
        else:
            conversion = note*0
            candidato.append(conversion)
        sum_+=conversion
    media = sum_/quantity
    candidato.append(media)
    total_candidatos.append(candidato[:])
cont = 0
while cont<len(total_candidatos):
    cont2 = 0
    while cont2<len(total_candidatos):
        if total_candidatos[cont][-1]>total_candidatos[cont2][-1]:
            total_candidatos[cont][-1], total_candidatos[cont2][-1] = total_candidatos[cont2][-1], total_candidatos[cont][-1]
        cont2+=1
    cont+=1

for n in range(quantity_total):
    print("%d° - %s - %7.2f" %((n+1), total_candidatos[n][0], total_candidatos[n][-1]))

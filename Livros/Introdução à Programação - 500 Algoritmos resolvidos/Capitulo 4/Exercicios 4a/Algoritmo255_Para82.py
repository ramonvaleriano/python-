# Program: Algoritmo255_Para82.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/202 - 09:37
# Updated:

higher = 5
cont_media = 0
media_total = 0
for e in range(higher):
    current = int(input("Enter with the quantity of students: "))
    cont_super = 0
    for n in range(current):
        media = float(input("Enter with the media of the %d student:" %(n+1)))
        cont_media+=media
        if media>=7:
            cont_super+=1
    print()
    media_turma = cont_super/current
    print(media_turma)
    media_total+=media_turma
media_total = media_total / higher
print()
print(media_total)

# Program: Algoritmo254_Para81.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/202 - 09:22
# Updated:

cont_number = 0
variable = False
higher = 20
current = 10
cont_team = 0

for e in range(higher):
    cont_note = 0
    for n in range(current):
        note = float(input("Enter with the %02d° note of the %02d° student: " %((n+1),(e+1))))
        if note>=0:
            cont_note+=note
            if note>=5:
                cont_number=+1
        else:
            variable = True
            break
    if variable:
        break
    media_student = cont_note/current
    print()
    print(media_student)
    print()
    cont_team+=cont_note

if variable == False:
    conversion =(100*cont_number)/higher
    media_team = cont_team/higher
    print()
    print(conversion)
    print(media_team)
else:
    print("Wrong, you are Asshole!")

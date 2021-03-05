# Program: Algoritmo348_Imprimedia.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 11:00
# Updated:

class_ = dict()
number_notes = 2
students = 2
for e in range(students):
    name = str(input("Enter with the student name: "))
    notas = list()
    sum_ = 0
    media = 0
    for g in range(number_notes):
        note = float(input("Enter with the %d note: " %(g+1)))
        notas.append(note)
        sum_+=note
    media = sum_/number_notes
    notas.append(media)
    class_[name]=notas
print()
for k, v in class_.items():
    print("The student name: ", k)
    cont = 0
    for n in v:
        if cont<=(len(class_.values())-1):
            print("The %d note: %5.2f" %((cont+1), v[cont]))
        else:
            print("The media: %5.2f" %media)
        cont+=1
    print()
    

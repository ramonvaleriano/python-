# Program: Algoritmo348_ImprimediaTeste.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 11:18
# Updated:

class_ = list()
number_students = 2
notes_ = 2

for e in range(number_students):
    dados = list()
    name = str(input("Enter with the %d° name: " %(e+1)))
    dados.append(name)
    sum_ = 0
    media = 0
    for n in range(notes_):
        note = float(input("Enter with the %d° note:" %(n+1)))
        dados.append(note)
        sum_+=note
    media = sum_/notes_
    dados.append(media)
    class_.append(dados)
    #del dados[0:]
    print()
print()
for x, g in enumerate(class_):
    cont = 0
    print("The %d sutdent: "%(x+1),g[cont])
    quantity = len(g)
    cont1 = 0
    quantity = len(g)
    for h in range(1, quantity):
        if h<(quantity-1):
            print("The %d note: %5.2f" %((h),g[h]))
        else:
            print("The media: %5.2f" %(media))
    print()

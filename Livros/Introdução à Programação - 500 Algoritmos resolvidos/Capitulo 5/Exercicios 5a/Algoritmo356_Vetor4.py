# Program: Algoritmo356_Vetor4.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 14:27
# Updated:

class_ = dict()
students = 15
notes_ = 2
for e in range(students):
    name = str(input("%d° Name: " %(e+1)))
    name = name.upper()
    sum_ = 0
    cont = 0
    media = 0
    dados = list()
    while cont<notes_:
        note = float(input("Enter with the %d° note: " %(cont+1)))
        if note >=0 and note <= 10:
            dados.append(note)
            sum_+=note
            cont+=1
        else:
            print("Invalid Option!")
    media = sum_/notes_
    print("Media: ", media)
    dados.append(media)
    class_[name] = dados
print("\n\n")
print(class_)
print("\n\n")

for k, v in class_.items():
    print("The name: ", k)
    cont = 0
    quantity = len(v)
    for n in v:
        if cont<(quantity-1):
            print("%d - %5.2f" %((cont), n))
        else:
            print("media = %5.2f" %n)
            if n>=7:
                print("Aprovado!")
            else:
                print("Reprovado!")
        cont+=1
        
    print("\n")

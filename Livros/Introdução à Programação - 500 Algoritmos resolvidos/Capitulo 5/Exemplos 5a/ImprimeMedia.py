# Program: ImprimeMedia.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 21/04/2020 - 16:27
# Updated:

class_ = []
quantity = 2
for e in range(quantity):
    sum_=0
    student = []
    media = 0
    name = input("Enter with name of the %d student: " %(e+1))
    name = name.upper()
    student.append(name)
    cont = 0
    while cont<2:
        note = float(input("Entre with the %d° note:" %(cont+1)))
        if note>=0:
            student.append(note)
            sum_+=note
            cont+=1
        else:
            print("Enter with a valid value!")
    media = sum_/cont
    student.append(media)
    print("\n")
    print(student)
    print("\n")
    class_.append(student)
#print(class_)

for n in class_:
    print("Name %s, 1° note: %5.2f, 2° note: %5.2f, media = %5.2f."
          %(n[0], n[1], n[2], n[3]))
    print("\n")

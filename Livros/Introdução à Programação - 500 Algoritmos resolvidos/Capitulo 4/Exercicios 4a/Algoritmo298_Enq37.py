# Program: Algoritmo298_Enq37.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 08:00
# Updated:

cont_aprovados = 0
cont_reprovados = 0
sum_note = 0
cont_student = 0
message = "OK"
media_classes = 0 

while True:
    classes = int(input("Enter with the number of classes: "))
    if classes == 0 or message == "NOK" :
        break
    for e in range(classes):
        students = int(input("Enter with the number of students of the classes %d: " %(e+1)))
        if students < 0 :
            message = "NOK"
            break 
        for n in range(students):
            note = float(input("Enter with the media of the Student %d: " %(n+1)))
            if note < 0 :
                break
            if note>=7:
                cont_aprovados+=1
            else:
                cont_reprovados+=1
            sum_note+=note
            cont_student+=1
        media_classes = sum_note/cont_student
        print(media_classes)
conversion = (cont_student*cont_reprovados)/100 
print()
print(cont_student)
print(conversion)

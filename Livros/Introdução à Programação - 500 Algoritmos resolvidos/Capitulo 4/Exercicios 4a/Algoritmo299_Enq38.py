# Program: Algoritmo299_Enq38.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 08:19
# Updated:

cont_aprovados = 0
cont_reprovados = 0
sum_note = 0
cont_student = 0
message = "OK"
media_classes = 0 
test = 5
mass = 0
cont_test_3 = 0

while True:
    classes = int(input("Enter with the number of classes: "))
    if classes == 0 or message == "NOK" :
        break
    for e in range(classes):
        students = int(input("Enter with the number of students of the classes %d: " %(e+1)))
        if students < 0 or message == "NOK" :
            message = "NOK"
            break 
        for n in range(students):
            if students < 0 :
                message = "NOK"
                break
            name = input("Enter with name of the student: ")
            for y in range(test):
                note = float(input("Enter with the not %d of the Student %d: " %((y+1) , (n+1))))        
                if note < 0 :
                    break
                if note>=7:
                    cont_aprovados+=1
                    if cont_aprovados == 5:
                        print("Aprovado em todas: %s" %name)
                if note>=7 and y == 0:
                    mass+=1
                if note>=7 and y == 3:
                    mass+=1
                    if mass == 2:
                        print("Aluno %s aprovado na primeira e terceira prova." %name)
                if note>=7 and y == 2:
                    cont_test_3+=1
                cont_student+=1
                sum_note+=note
            mass = 0
            cont_aprovados = 0
        media_classes = sum_note/cont_student
        print(media_classes)           
conversion = (cont_student*cont_test_3)/100 
print()
print(cont_student)
print(conversion)


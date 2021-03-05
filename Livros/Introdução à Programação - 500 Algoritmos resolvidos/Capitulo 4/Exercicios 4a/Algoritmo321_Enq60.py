# Program: Algoritmo321_Enq60.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 10/04/2020 - 10:14
# Updated:

cont_failed = 0

while True:
    number_of_classes = int(input("Enter with the number of the classes: "))
    if number_of_classes == "*":
        break
    classes = int(input("Enter whit the quantity the classes: "))
    number_students = int(input("Enter with the number of students: "))
    for e in range(number_students):
        absences = int(input("Enter with the number of absences of the student %d" %(e+1)))
        media_student = (absences*classes)/100
        if media_student > 25:
            cont_failed+=1
            print("Failed Student!")
print()
print(cont_failed)

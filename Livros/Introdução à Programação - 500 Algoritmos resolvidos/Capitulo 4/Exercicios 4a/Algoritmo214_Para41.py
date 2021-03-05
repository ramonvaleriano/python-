# Program: Algoritmo214_Para41.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 17:57
# Updated:

sum_ = 0
sum_student = 0
current = 15
media_student = 0
media = 0

for e in range(current):
    name = input("Enter with your name: ")
    note1 = int(input("Enter with your first note: "))
    note2 = int(input("Enter with your first note: "))
    sum_student = note1+note2
    media_student = sum_student/2
    sum_+= media_student
    print(name)
    print(media_student)
    print("\n")
media = sum_/current
print(media)

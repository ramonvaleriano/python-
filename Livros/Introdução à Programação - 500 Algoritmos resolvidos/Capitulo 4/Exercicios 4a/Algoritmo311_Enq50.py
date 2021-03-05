# Program: Algoritmo311_Enq50.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 07/04/2020 - 10:07
# Updated:

sum_note = 0
bigger = 0
while True:
    registration = int(input("Enter with the registration: "))
    if registration<1 or registration>5000:
        break
    courses = int(input("Enter with the numbers courses: "))
    for e in range(courses):
        note = float(input("Enter with the %d° note: " %(e+1)))
        if note<0:
            message = "NOK"
        sum_note+=note
    cr = sum_note/courses
    if cr>=bigger and courses>=5:
        bigger = cr
    print(cr)
    print(courses)
    print()
print()
print(bigger)
print()
    

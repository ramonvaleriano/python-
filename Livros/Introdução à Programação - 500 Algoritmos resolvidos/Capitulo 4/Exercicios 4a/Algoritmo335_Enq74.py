# Program: Algoritmo335_Enq74.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/04/2020 - 19:12
# Updated:

bigger = 0
cont = 0
cont_blonde = 0

while True:
    age = int(input("Enter with your age: "))
    if age <= 0:
        break
    if age >= bigger:
        bigger = age
        
    sex = input("Enter with your sex: ")
    sex = sex.upper()
    eye_color = input("Enter with eye color: ")
    eye_color = eye_color.upper()
    hair_color = input("Enter with hair color: ")
    hair_color = hair_color.upper()
    if ((sex == "FEMALE") and (eye_color == "GREEN") and (hair_color == "BLONDE") and
        ((age>=18)and(age<=35))):
        cont_blonde+=1
    cont+=1
media = (cont*cont_blonde)/100
print(bigger)
print(media)

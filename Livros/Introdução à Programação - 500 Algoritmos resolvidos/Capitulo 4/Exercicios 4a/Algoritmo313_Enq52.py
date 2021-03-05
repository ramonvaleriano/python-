# Program: Algoritmo313_Enq52.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 07/04/2020 - 10:32
# Updated:

higher = 0
sum10_20 = 0
cont10_20 = 0
cont40 = 0
cont =0
#nothing = 0

while True:
    age = int(input("Enter with your age: "))
    if age <=0 :
        break
    height = float(input("Enter with your height: "))
    weight = float(input("Ener with your weight: "))
    if ((age>=10) and (age<=20)):
        cont10_20+=1
        sum10_20+=height
    elif age>=50:
        higher+=1
    #else:
        #nothing+=1

    if weight <= 40:
        cont40+=1
    cont+=1
media = sum10_20/cont10_20
converstion = (cont*cont40)/100
print()
print(media)
print(higher)
print(converstion)
print()

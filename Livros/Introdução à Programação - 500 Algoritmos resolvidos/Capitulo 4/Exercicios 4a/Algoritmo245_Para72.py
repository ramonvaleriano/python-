# Program: Algoritmo245_Para72.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/202 - 07:51
# Updated:

sum1=0
sum2=0
sum3=0
sum4=0
cont1=0
cont2=0
cont3=0
cont4=0

for e in range(20):
    name = input("Enter with your name: ")
    weight = float(input("Enter with your weight: "))
    age = int(input("Enter with your age: "))
    if age>=1 and age<11:
        cont1+=1
        sum1+=weight
    elif age>=11 and age<20:
        cont2+=1
        sum2+=weight
    elif age>=20 and age<30:
        cont3+=1
        sum3+=weight
    elif age>=30:
        cont4+=1
        sum4+=weight
    else:
        print("You are asshole!")
media1 = sum1/cont1
media2 = sum2/cont2
media3 = sum3/cont3
media4 = sum4/cont4
print()
print(media1)
print(media2)
print(media3)
print(media4)

# Program: Algoritmo310_Enq49.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 07/04/2020 - 09:45
# Updated:

channel = int(input("Enter whit the TV Channel: "))
people = int(input("Enter with quantity of people: "))
audience_4 = 0
audience_5 = 0
audience_7 = 0
audience_12 = 0
quantity4 = 0
quantity5 = 0
quantity7 = 0
quantity12 = 0
cont_nothing = 0
people_total = 0


while channel>=0:
    if channel == 4:
        audience_4+=1
        quantity4+=people
    elif channel == 5:
        audience_5+=1
        quantity5+=people
    elif channel == 7:
        audience_7+=1
        quantity7+=people
    elif channel == 12:
        audience_12+=1
        quantity12+=people
    else:
        cont_nothing+=1
    people_total+=people
    channel = int(input("Enter whit the TV Channel: "))
    people = int(input("Enter with quantity of people: "))
print()
result4 = (people_total*quantity4)/100
result5 = (people_total*quantity5)/100
result7 = (people_total*quantity7)/100
result12 = (people_total*quantity12)/100
print()
print(audience_4)
print(result4)
print()
print(audience_5)
print(result5)
print()
print(audience_7)
print(result7)
print()
print(audience_12)
print(result12)

# Programa: Algoritmo136_se47.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 13:46
# Updated:

name = input("Enter with your name: ")
age = int(input("Enter with your age: "))

test = type(age) is int
name = name.upper()

if(test == True)and(age>=0):
    if (age>=0)and(age<=10):
        value = 10
    elif(age>=11)and(age<=29):
        value = 60
    elif(age>=30)and(age<=45):
        value = 120
    elif(age>=46)and(age<=59):
        value = 150
    elif(age>=59)and(age<=65):
        value = 250
    else:
        value = 400
else:
    value = 0
print(name)
print(value)
        

# Programa: Algoritmo134_se45.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 12:57
# Updated:

age = int(input("Enter with the your age: "))

if(type(age) is int)and(age>0):
    if(age>=5)and(age<=7):
        message = "Infantil A"
    elif(age>=8)and(age<=10):
        message = "Infantil B"
    elif(age>=11)and(age<=13):
        message = "Juvenil A"
    elif(age>=14)and(age<=17):
        message = "Juvenil B"
    elif age>17:
        message = "Sênio"
    else:
        message = "What fuck is this?!"
else:
    print("You are asshole!")
print(message)
    

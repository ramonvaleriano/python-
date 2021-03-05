# Program: Algoritmo125_se36.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 09:46
# Updated:

age = int(input("Enter with your age: "))

test = type(age) is int

if(age<18)and(age>=0):
    message = "Minor!"
elif(age>=18)and(age<65):
    message = "Older!"
elif age>=65:
    message = "Old man!"
else:
    message = "What fuck is this?!"

print("%s" %message)
    

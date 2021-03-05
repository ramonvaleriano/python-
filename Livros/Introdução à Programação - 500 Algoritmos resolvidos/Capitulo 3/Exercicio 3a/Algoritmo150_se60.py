# Program: Algoritmo150_se60.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 11:49
# Updated:

value = float(input("Enter with the value: "))

if value>0:
    if value<=10:
        tax = 70
    elif(value>10)and(value<=30):
        tax = 50
    elif(value>30)and(value<=50):
        tax = 40
    else:
        tax = 30
    conversion = value + ((value*tax)/100)
else:
    print("You are wrong!")
print(conversion)

    

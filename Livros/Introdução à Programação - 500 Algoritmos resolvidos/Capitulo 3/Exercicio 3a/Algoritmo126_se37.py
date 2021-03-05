# Program: Algoritmo126_se37.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 10:33
# Updated:

number = float(input("Enter with a number: "))

if number == 5:
    message = "This number is 5!"
elif number == 200:
    message = "This number is 200!"
elif number == 400:
    message = "This number is 400!"
elif(number>=500)and(number<=1000):
    message = "This number is between 500 and 1000"
else:
    message = "You are asshole!"

print(message)

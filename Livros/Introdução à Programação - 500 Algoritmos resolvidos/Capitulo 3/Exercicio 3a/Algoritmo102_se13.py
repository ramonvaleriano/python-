# Program: Algoritmo102_se13.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/03/2020 - 12:05
# Updated:

number = float(input("Enter with a number: "))

if number < 20:
    message = "This number less than 20!"
elif number > 20:
    message = "This greater than 20!"
else:
    message = "This equal to 20!"
print(message)

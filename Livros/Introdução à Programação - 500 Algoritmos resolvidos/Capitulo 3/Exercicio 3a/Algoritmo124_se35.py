# Program: Algoritmo124_se35.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 09:33
# Updated:

number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))
number3 = float(input("Enter with the third number: "))

if((number1<(number2+number3))and(number1<(number2+number3))and
   (number1<(number2+number3))):

    #print("This program works so far!")
    if(number1>number2)and(number1>number3):
        higher = number1
        sice = (number2**2) + (number3**2)
    if(number2>number1)and(number2>number3):
        higher = number2
        sice = (number1**2) + (number3**2)
    if(number3>number2)and(number3>number1):
        higher = number3
        sice = (number2**2) + (number1**2)
    #else:
        #higher = 0
        #sice = 0
    if(higher==sice):
        message = "Triangulo Retangulo!"
    if(higher>sice):
        message = "Triangulo Obusangulo!"
    if(higher<sice):
        message = "Triangulo Retangulo!"
else:
    print("What fuck is this:")

print(message)
print(higher)
print(sice)

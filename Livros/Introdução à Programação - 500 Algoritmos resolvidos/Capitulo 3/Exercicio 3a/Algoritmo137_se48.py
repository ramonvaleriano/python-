# Programa: Algoritmo137_se48.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 14:01
# Updated:

import math

number1 = int(input("Enter with the first number: "))
number2 = int(input("Enter with the Second number: "))
number3 = int(input("Enter with the third number: "))

if(type(number1) is int)and(type(number1) is int)and(type(number1) is int):
    if number1 == 0:
        print("Is not second defreen equation!")
    else:
        delta = (number2**2)-(4*number1*number3)
        if delta >= 0:
            result1 = ((number2*-1)+(math.sqrt(delta)))/(2*number1)
            result2 = ((number2*-1)-(math.sqrt(delta)))/(2*number1)
            if result1 == result2:
                print(result1)
            else:
                print(result1)
                print(result2)
                
        else:
            print("Não há raizes!")
else:
    print("What fuck is this?!")

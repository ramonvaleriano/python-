# Program: Algoritmo284_Enq23.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 17:26
# Updated:

cont = 1

while True:
    number = int(input("Enter with the %d° number: " %cont))
    if number==-9999:
        break
    elif number >= 10 and number%10==0:
        result = int(number/10)
        if result%cont==0:
            print(result)
    cont+=1  

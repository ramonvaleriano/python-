# Program: Listagem6_7.py
# Author: Ramon R. Valeriano
# Description:  
# Developed: 19/04/2020 - 13:28
# Updated:

numbers = [0,0,0,0,0]
cont = 0
while cont<len(numbers):
    numbers[cont] = float(input("Enter with %d° number: " %(cont+1)))
    cont+=1
while True:
    chosen = int(input("What position do you want: "))
    if chosen == 0:
        break
    elif chosen>0 and chosen<=5:
        print(numbers[chosen-1])
    else:
        print("Invalid Option!")

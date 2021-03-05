# Program: Algoritmo206_Para32.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 13:35
# Updated:

quantity = int(input("Enter with the quantity number of repetition: "))
if quantity > 0:    
    number = int(input("Enter with the 1° number: "))
    bigger = number
    smaller = number
    for e in range(1, quantity):
        number = int(input("Enter with the %d° number: " %(e+1)))
        if number>=bigger:
            bigger = number
        elif number<=smaller:
            smaller=number
        
    print("\n",bigger)
    print("\n",smaller)
else:
    print("Invalid Option!")

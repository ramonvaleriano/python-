# Program: Algotimo318_Enq57.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 08/04/2020 - 12:19
# Updated:

while True:
    complete = input("Enter with your full name: ")
    if complete == "@":
        break
    quantity = len(complete)
    n = quantity-1
    cont = 0
    while n>=0:
        test = complete[n]
        if ( test == " ")and(test != (quantity-1)):
            break
        n-=1
    last_name = complete[n:]
    print(last_name)
    
        

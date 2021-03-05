# Program: Algoritmo336_Enq75.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/04/2020 - 19:31
# Updated:

total = 0

while True:
    sum_ = 0
    tax = 0
    children = int(input("Enter with the number of children: "))
    if children <= 0:
        break

    elif children > 0:
        for e in range(1, children+1):
            option = int(input("Enter with schooling of the %d° child: " %e))
            if option == 1:
                value = 300
                result = value - ((value*tax)/100)
                tax+=10
            elif option == 2:
                value = 400
                result = value - ((value*tax)/100)
                tax+=10
            elif option == 3:
                value = 500
                result = value - ((value*tax)/100)
                tax+=10
            elif option == 4:
                value = 600
                result = value - ((value*tax)/100)
                tax+=10
            else:
                print("Invalid Option: ")
            sum_+=result
        print(sum_)
        total+=sum_
    else:
        print("Invalid Option: ")
print(total)
            
            



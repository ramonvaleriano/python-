# Program: Algoritmo292_Enq31.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/04/2020 - 09:09
# Updated:

cont = 0
number = float(input("Enter with the %d° number" %(cont+1)))
bigger = number
smaller = number
if number >= 10 and number%10==0:
    while number!=0:
        if number >= 10 and number%10==0:
            cont+=1
            sum_+=number
            if number>=bigger:
                bigger = number
            elif number<=smaller:
                smaller = number
        else:
            print("Try Again")
        number = float(input("Enter with the %d° number" %(cont+1)))
else:
            print("Try Again")
            cont = 1
media = sum_/cont
print(bigger)
print(smaller)
print(media)

        
        

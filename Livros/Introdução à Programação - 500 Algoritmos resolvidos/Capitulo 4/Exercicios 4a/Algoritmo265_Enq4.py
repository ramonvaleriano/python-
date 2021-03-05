# Program: Algoritmo265_Enq4.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 11:13
# Updated:

cont = 0
number = int(input("Enter with a number %d°: " %(cont+1)))
cont_n = 0
while number!=0:
    cont+=1
    if number>=100 and number<=200:
        cont_n+=1
    number = int(input("Enter with a number %d°: " %(cont+1)))
print(cont_n)
    
    

# Program: Algoritmo278_Enq17.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 10:15
# Updated:



number = int(input("Enter with a number: "))
cont = 0
while number>0:
    for e in range(1, number+1):
        if number%e==0:
            cont+=1
            
    if cont==2:
        print("It is prime number! ")
    else:
        print("It is not prime number! ")
    number = int(input("Enter with a number: "))
    cont = 0

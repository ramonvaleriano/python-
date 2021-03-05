# Program: Algoritmo275_Enq14.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 09:45
# Updated:

cont = 0
factorial = 1

while True:
    number = int(input("Enter with the %d° number: " %(cont+1)))
    factorial = 1
    if number<1:
        break
    for e in range(1, number+1):
        factorial*=e
    print(factorial)
    cont+=1

# Program: Algoritmo100_se11.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/03/2020 - 09:39
# Updated:

number = int(input("Enter with a interger: "))

if ((number>=1000)and(number<=9999)):
    thousand = int(number/1000)
    hundred = int((number%1000)/100)
    ten = int((number%100)/10)
    unity = number%10

    print(thousand)
    print(hundred)
    print(ten)
    print(unity)
    if((thousand%4==0)and(hundred%4==0)):
        print("It is numbers %d and %d are divisible by four!" %(thousand, hundred))
    else:
        print("Is is not divisible!")
else:
    print("You are asshole!")

    

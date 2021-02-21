# Program: Exercicio5_12.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 07:54
# Updated: 

balance = float(input("Enter with your balance: "))
tax = float(input("Enter with your tax: "))
cont = 0
conversion = 0
sum_conversion = 0
if(balance>0)and(tax>0):
    conversion = (balance*tax)/100
    sum_conversion+=conversion
    print(conversion, "\n")
    while cont<=24:
        balance = float(input("Enter with your balance: "))
        conversion = (balance*tax)/100
        sum_conversion+=conversion
        print(conversion, "\n")
        cont+=1
    print(sum_conversion, "\n\n")
else:
    print("You are asshole!")

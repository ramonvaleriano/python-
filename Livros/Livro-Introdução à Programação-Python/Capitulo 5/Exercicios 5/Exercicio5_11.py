# Program: Exercicio5_11.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 07:27
# Updated: 30/03/2020 - 08:05

balance = float(input("Enter with your balance: "))
tax = float(input("Enter with your tax: "))
cont = 1
conversion = 0
sum_conversion = 0
sum_balance = 0
if(balance>0)and(tax>0):
    conversion = (balance*tax)/100
    #sum_conversion+=conversion
    sum_balance=balance+conversion
    print(conversion, "\n")
    while cont<=24:
        conversion = 0
        sum_balance+=balance
        conversion = (sum_balance*tax)/100
        total = sum_balance + conversion  
        print(total)
        cont+=1
        
    print(sum_balance, "\n\n")
else:
    print("You are asshole!")

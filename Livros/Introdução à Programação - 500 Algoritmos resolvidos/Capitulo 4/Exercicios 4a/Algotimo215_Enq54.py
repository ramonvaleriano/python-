# Program: Algotimo215_Enq54.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 08/04/2020 - 11:16
# Updated:

tax_boy = 11
tax_girl = 12
value_girl = 0
value_boy = 0
result = 0
cont_family = 0

while True:
    family = input("Entet with the name of the family: ")
    family = family.upper()
    if family == "@":
        break
    print("The family have Children: ")
    answer = input("Enter wiht Yes or Not: ")
    answer = answer.upper()
    
    if answer == "YES":
        boy = int(input("Enter with the quantity of Boys: "))
        if boy>0:
            value_boy=tax_boy*boy
        else:
            value_boy = 0
            
        girl = int(input("Enter with the quantity of girl: "))
        if girl>0:
            value_girl=tax_girl*girl
        else:
            value_girl = 0
        print()
        print(family)
        print(value_boy)
        print(value_girl)
        print()
        result = value_girl + value_boy
        cont_family+=1
        
    elif answer == "NOT":
        result = value_girl + value_boy
        cont_family+=1

    else:
        print("Invalid Option!")
    
print()
print(cont_family)
print(value_girl)
print(value_boy)

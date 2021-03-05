# Program: Algoritmo333_Enq72.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 23:11
# Updated:

number = 1

while number>=1 and number<=7:
    number = int(input("Enter with the option: "))
    if number == 1:
        tax = 100
    elif number == 2:
        tax = 80
    elif number == 3:
        tax = 50
    elif number == 4:
        tax = 30
    elif number == 5:
        tax = 10
    elif number == 6:
        tax = 5
    elif number == 7:
        tax = 0
    salary = float(input("Enter with your salary: "))
    new_salary = salary + ((salary*tax)/100)
    print(new_salary)
    

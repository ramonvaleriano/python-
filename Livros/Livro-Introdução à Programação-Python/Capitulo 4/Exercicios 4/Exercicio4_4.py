# Program: Exercicio4_4.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 13:02
# Updated:

salary = float(input("Enter with the salary: R$ "))

if (salary>0):
    if salary <= 1250:
        tax = 15
    else:
        tax = 10
    new_salary = salary + ((salary*tax)/100)
    print("The new salary is: R$ %5.2f" %new_salary)
else:
    print("Você é retardado!")
        
    

# Program: Algoritmo234_Para61.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 02/04/2020 - 22:47
# Updated:

higher = 10

for e in range(higher):
    name = input("Enter with your name: ")
    salary = float(input("Enter with your salary: "))
    if salary>0 and salary<=600:
        tax = 0
    elif salary>600 and salary<=1500:
        tax = 10
    elif salary>1500:
        tax = 15
    else:
        tax = 0
        print("You are asshole!")
    new_salary = salary - ((salary*tax)/100)
    print("\n", name)
    print("\n", new_salary, "\n")


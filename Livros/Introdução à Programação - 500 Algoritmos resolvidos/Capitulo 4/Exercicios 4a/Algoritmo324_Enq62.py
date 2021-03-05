# Program: Algoritmo324_Enq62.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 19:26
# Updated:

bigger = 0
higher = 0
cont_regurlar = 0
sum_regular = 0

while True:

    registration = int(input("Enter with your registration: "))
    if registration < 0:
        break
    salary = float(input("Enter with your salary: "))
    option = input("Enter with your option: ")
    option = option.upper()
    
    tax = 0
    if option == "EXCELENTE":
        tax = 80
        new_salary = salary + ((salary*tax)/100)
        print(new_salary)
    elif option == "BOM":
        tax = 50
        new_salary = salary + ((salary*tax)/100)
        print(new_salary)
    elif option == "REGULAR":
        tax = 30
        new_salary = salary + ((salary*tax)/100)
        cont_regurlar+=1
        sum_regular+=new_salary
        print(new_salary)
    else:
        tax = 0
        print("Invalid Option")

    if new_salary>=bigger:
        bigger = new_salary
        higher = registration
media = cont_regurlar/sum_regular
print()
print(bigger)
print(higher)
print(media)
    

# Programa: Algoritmo129_se40.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 11:54
# Updated:

salary = float(input("Enter with the your salary: "))

if salary > 0:
    if salary <= 600:
        tax = 0
    elif(salary>600)and(1200):
        tax = 20
    elif(salary>1200)and(2000):
        tax = 25
    else:
        tax = 30
else:
    tax = 0
    print("What fuck is this?!")

discount = salary - ((salary*tax)/100)
print(discount)

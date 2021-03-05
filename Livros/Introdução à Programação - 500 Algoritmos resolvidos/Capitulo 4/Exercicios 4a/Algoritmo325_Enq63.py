# Program: Algoritmo325_Enq63.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 19:42
# Updated:

sum_worked = 0
worked_hours = 0

while True:
    minium_salary =  float(input("Enter with the value of the minimum salary: "))
    if minium_salary < 0:
        break
    while worked_hours > -1:
        sum_worked+=worked_hours
        worked_hours = float(input("Enter with quantity of the worked hours: "))
    dependents = int(input("Enter with number of dependents: "))
    overtime = float(input("Enter with the number of overtime: "))
    work_value = minium_salary/10
    salary = work_value*sum_worked
    
    if dependents > 0:
        salary = salary + (dependents*32)
    if overtime > 0:
        extra = (work_value*50)/100
        value_overtime = extra * overtime
        salary = salary +  value_overtime

    if salary <= 900:
        tax = 0
        bonus = 100
    elif salary > 900 and salary <= 1500:
        tax = 10
        bonus = 50
    elif salary > 1500:
        tax = 20
        bonus = 50
    else:
        tax = 0
        bonus = 0
    salary = (salary - ((tax*salary)/100)) +  bonus    
    print(salary)
    

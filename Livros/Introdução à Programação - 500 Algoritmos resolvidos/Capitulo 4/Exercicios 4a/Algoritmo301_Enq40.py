# Program: Algoritmo301_Enq40.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 09:41
# Updated:

total_spend = 0
cont_higher_200 = 0
cont_personal = 0
cont = 0

while True:
    personal_income = float(input("Enter with your personal income: "))
    if personal_income < 0 :
        break
    family_income =  float(input("Enter with the family income: "))
    food_expenses = float(input("Enter with the food expenses:"))
    other_expenses = float(input("Enter with the other expenses: "))
    
    if other_expenses > 200:
        cont_higher_200+=1
    if personal_income >= family_income:
        cont_personal+=1

    total_expenses = food_expenses + other_expenses
    if personal_income >= total_expenses:
        food_percentage = (personal_income*food_expenses)/100
        other_percentage = (personal_income*other_expenses)/100
        print(food_percentage)
        print(other_percentage)
    else:
        print("The Expensive is greater than personal income!")

    if family_income >= total_expenses:
        food_percentage2 = (family_income*food_expenses)/100
        other_percentage2 = (family_income*other_expenses)/100
        print(food_percentage2)
        print(other_percentage2)
    else:
        print("The Expensive is greater than family income!")
    cont+=1
conversion = (cont*cont_higher_200)/100
print()
print(conversion)
print(cont_personal)

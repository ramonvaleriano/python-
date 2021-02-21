# Program: Exercicio5_13.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 08:05
# Updated:

debt = float(input("Enter with value of the debit: "))
tax = float(input("Enter with value of the tax: "))
monthly_value =  float(input("Enter with monthly value: "))
new_debt = debt + ((debt*tax)/100)
total = new_debt
quantity_month=0
extra_month = 0
if debt>0 and tax>=0 and monthly_value > 0 and debt >= monthly_value:
    #new_debit = debit + ((debit*tax)100)
    #print("\n",new_debit,"\n")
    while new_debt>=monthly_value:
        new_debt-=monthly_value
        quantity_month+=1
    rest = new_debt
    if rest!=0:
        extra_month+=1
    interest = total - debt
    print(total)
    print(interest)
    print(quantity_month)
    print(extra_month)
    print(rest)
else:
    print("You are asshole!")
    
    
    

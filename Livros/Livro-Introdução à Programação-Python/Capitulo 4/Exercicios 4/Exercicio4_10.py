# Program: Exercicio4_10.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 15:38
# Updated:

type_ = input("Enter with the Type: ")
quantity = float(input("Enter with the quantity: "))

if (type_ == "R")or(type_ == "r"):
    if quantity <= 500:
        tax = 0.40
    elif quantity > 500:
        tax = 0.65
    else:
        tax = 0
        print("You are Asshole!")
elif (type_ == "C")or(type_ == "c"):
    if quantity <= 1000:
        tax = 0.55
    elif quantity > 1000:
        tax = 0.60
    else:
        tax = 0
        print("You are Asshole!")
elif (type_ == "I")or(type_ == "i"):
    if quantity <= 5000:
        tax = 0.55
    elif quantity > 5000:
        tax = 0.60
    else:
        tax = 0
        print("You are Asshole!")
else:
    print("Your are Asshole!")

result = quantity * tax
print(result)

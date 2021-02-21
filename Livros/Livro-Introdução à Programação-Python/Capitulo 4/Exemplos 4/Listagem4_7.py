# Program: Listagem4_7.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 15:05
# Updated:

category = int(input("Enter with the category: "))

if category == 1:
    value = 10
else:
    if category == 2:
        value = 18
    else:
        if category == 3:
            value = 23
        else:
            if category == 4:
                value = 26
            else:
                if category == 5:
                    value = 18
                else:
                    print("Your are an asshole!")
                    value = 0
print(value)

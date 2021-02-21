# Program: Exercicio4_3.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 11:34
# Updated: 23/03/2020 - 12:56

number1 = int(input("Enter with the first number: "))
number2 = int(input("Enter with the second number: "))
number3 = int(input("Enter with the third number: "))

if (number1>=number2)and(number1>=number3):
    bigger = number1
    if number2 >= number3:
        smaller = number3
    else:
        smaller = number2
elif (number2>=number3):
    bigger = number2
    if number1 >= number3:
        smaller = number3
    else:
        smaller = number1
else:
    bigger = number3
    if number1 >= number2:
        smaller = number2
    else:
        smaller = number1

print("The number larger: %d\nThe number smaller: %d" %(bigger, smaller))
        

# Program: Algoritmo141_se52.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 21:59
# Updated: 26/03/2020 - 08:09

name1 = input("Enter with the firt name: ")
number1 = float(input("Enter with the firt number:"))
name2 = input("Enter with the second name: ")
number2 = float(input("Enter with the second number:"))
name3 = input("Enter with the third name: ")
number3 = float(input("Enter with the third number:"))

if(number1>=number2)and(number1>=number2):
    bigger = number1
    if(number2>=number3):
        smaller = number3
        medio = number2
        print("%s - %5.2f"%(name1, bigger))
        print("%s - %5.2f"%(name2, medio))
        print("%s - %5.2f"%(name3, smaller))
    else:
        smaller = number2
        medio = number3
        print("%s - %5.2f"%(name1, bigger))
        print("%s - %5.2f"%(name3, medio))
        print("%s - %5.2f"%(name2, smaller))
    
elif number2>=number3:
    bigger = number2
    if number1>=number3:
        smaller = number3
        medio = number1
        print("%s - %5.2f"%(name2, bigger))
        print("%s - %5.2f"%(name1, medio))
        print("%s - %5.2f"%(name3, smaller))
    else:
        smaller = number1
        medio = number3
        print("%s - %5.2f"%(name2, bigger))
        print("%s - %5.2f"%(name3, medio))
        print("%s - %5.2f"%(name1, smaller))
else:
    bigger = number3
    if number1>=number2:
        smaller = number2
        medio = number1
        print("%s - %5.2f"%(name3, bigger))
        print("%s - %5.2f"%(name1, medio))
        print("%s - %5.2f"%(name2, smaller))
    else:
        smaller = number1
        medio = number2
        print("%s - %5.2f"%(name3, bigger))
        print("%s - %5.2f"%(name2, medio))
        print("%s - %5.2f"%(name1, smaller))

# Program: Algoritmo121_se32.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 08:14
# Updated: 25/03/2020 - 08:49

number1 = float(input("Enter with the firts number: "))
number2 = float(input("Enter with the second number: "))
number3 = float(input("Enter with the third number: "))
number4 = float(input("Enter with the fourth number: "))
number5 = float(input("Enter with the fifth number: "))

if((number1!=number2)and(number1!=number3)and(number1!=number4)and(number1!=number5)and
   (number2!=number3)and(number2!=number4)and(number2!=number5)and(number3!=number4)and
   (number3!=number5)and(number4!=number5)):

    #print("This programa works so far!")
    if((number1>number2)and(number1>number3)and(number1>number4)and(number1>number5)):
        higher = number1
        if((number2<number3)and(number2<number4)and(number2<number5)):
            smallest = number2
        elif((number3<number4)and(number3<number5)):
            smallest = number3
        elif number4<number5:
            smallest = number4
        else:
            smallest = number5
            
    elif((number2>number3)and(number2>number4)and(number2>number5)):
        higher = number2
        if((number1<number3)and(number1<number4)and(number1<number5)):
            smallest = number1
        elif((number3<number4)and(number3<number5)):
            smallest = number3
        elif number4<number5:
            smallest = number4
        else:
            smallest = number5

    elif((number3>number4)and(number3>number5)):
        higher = number3
        if((number1<number2)and(number1<number4)and(number1<number5)):
            smallest = number1
        elif((number2<number4)and(number2<number5)):
            smallest = number2
        elif number4<number5:
            smallest = number4
        else:
            smallest = number5

    elif number4>number5:
        higher = number4
        if((number1<number2)and(number1<number3)and(number1<number5)):
            smallest = number1
        elif((number2<number3)and(number2<number5)):
            smallest = number2
        elif number3<number5:
            smallest = number3
        else:
            smallest = number5
        
    else:
        higher = number5
        if((number1<number2)and(number1<number3)and(number1<number4)):
            smallest = number1
        elif((number2<number3)and(number2<number4)):
            smallest = number2
        elif number3<number4:
            smallest = number3
        else:
            smallest = number4
    
    #print("This programa works so far!")
    print(higher)
    print(smallest)

# Program: Exercicio5_4.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 28/03/2020 - 21:32
# Update:

end = float(input("Enter with a number"))

number = 1

if end>=1:
    while number<=end:
        if number%2!=0:
            print(number)
        number+=1
else:
    print("What fuck is this?!")

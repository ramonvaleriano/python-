# Program: Exercicio5_7.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 29/03/2020 - 11:49
# Update:

number = int(input("Enter with a number: "))
start = int(input("Enter with the start: "))
end = int(input("Enter with the End: "))

if start<=end:
    while start<=end:
        result = start*number
        print("%03d * %03d = %03d"%(start, number, result))
        start+=1
else:
    print("You ate asshole!")

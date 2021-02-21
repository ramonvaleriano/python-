# Program: Exercicio5_14.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 08:58
# Updated:

sum_ = 0
cont = 0
test1 = "OK"
while True:
    number = int(input("Enter with number: "))
    test = type(number) is int
    if test==False:
        test1 = "NOK"
        break
    if number == 0:
        break
    cont+=1
    sum_+=number
if test1 == "NOK":
    print("You are Asshole")
else:
    media = sum_/cont
    print(cont)
    print(media)
    print(sum_)

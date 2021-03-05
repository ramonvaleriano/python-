# Program: Algoritmo339_Enq78.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/04/2020 - 18:10
# Updated: 16/04/2020 - 18:45

while True:

    number = int(input("Enter with a number: "))
    if number%2!=0:
        break
    #number1= int(number+1)
    #list1 = list(range(1, number1))
    list1 = list(range(1, number))
    list2 = []
    for n in list1:
        cont = 0
        for e in range(1, number+1):
            if n%e==0:
                cont+=1
        if cont == 2 or n == 1:
            list2.append(n)
    print(list2)
    list3 = list2[:]

    for r in list2:
        for g in list3:
            test = r+g
            if test == number:
                print("%d + %d = %d" %(r, g, number))

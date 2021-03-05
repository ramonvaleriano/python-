# Program: Algoritmo329_Enq68.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 21:54
# Updated:

cont1 = 0
cont2 = 0
cont3 = 0
cont5 = 0
cont4 = 0
cont6 = 0

while True:
    code = int(input("Enter with code of the candidate: "))
    if code < 0:
        break
    if code == 1:
        cont1+=1
    elif code == 2:
        cont2+=1
    elif code == 3:
        cont3+=1
    elif code == 4:
        cont4+=1
    elif code == 5:
        cont5+=1
    elif code == 6:
        cont6+=1
    else:
        print("Invalid Option!")
sum_total = cont1 + cont2 + cont3 + cont4 + cont5 + cont6
conversion1 = (cont5*sum_total)/100
conversion2 = (cont6*sum_total)/100
print(cont1)
print(cont2)
print(cont3)
print(cont4)
print(cont5)
print(cont6)
print(conversion1)
print(conversion2)

# Program: Exercicio6_3.py
# Author: Ramon R. Valeriano
# Description:  
# Developed: 19/04/2020 - 17:52
# Updated:

l1 = list()
l2 = []
l5 = []
l5 = list()
while True:
    print("The firt List!")
    number1 = float(input("Enter with a number: "))
    if number1 == 0:
        break
    l1.append(number1)

while True:
    print("The second List!")
    number2 = float(input("Enter with a number: "))
    if number2 == 0:
        break
    l2.append(number2)

quantity = len(l1) + len(l2)
#print("A quantitdade de elementos: ", quantity)

cont = 0

#while cont<quantity:
#    print(cont)
#    cont+=1

l4=l1[:]
l5=l2[:]

for e in l4:
    for n in e:
        if n == e:
            del n

l3 = l4 + l5
print(l3)

           

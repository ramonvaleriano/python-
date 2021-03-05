# Program: Algoritmo362_Vetor10.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 19:44
# Updated:

list1 = list()
list2 = list()
list3 = list()
quantity1 = 10
quantity2 = 20

for e in range(quantity1):
    number = int(input("Enter with %d number:" %(e+1)))
    list1.append(number)
for n in range(quantity2):
    number = int(input("Enter with %d number:" %(n+1)))
    list2.append(number)
for g in list1:
    cont = 0
    for y in list2:
        if g == y:
            cont+=1
            if cont<2:
                list3.append(g)
#test_q = len(list3)
#for k in range(test_q):
#    for h in range((k+1), test_q):
#       if h == k:
#           del list3[k]
print()
print(list3)
        
        

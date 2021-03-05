# Program: Algoritmo352_ProcuraNomePeloNome2.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 13:29
# Updated:

dicionario = dict()
cont = 0
quantity = 3
for e in range(quantity):
    name = str(input("Enter with the %d° name: " %(e+1)))
    name = name[0].upper()+name[1:].lower()
    dicionario[name]= cont
    cont+=1
print(dicionario)
print("\n")
find  = True
while find:
    test = str(input("Enter with the number: "))
    test = test[0].upper()+test[1:].lower()
    for k, v in dicionario.items():
        if test == k:
            print(k)
            print(v)
            find = False
            break
    else:
        print("Invalid Option!")

# Program: Algoritmo352_ProcuraNomePeloNome.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 13:19
# Updated:

nomes = list()
quantity = 3
for e in range(quantity):
    name = str(input("Enter with the %d° name: " %(e+1)))
    name = name[0].upper()+name[1:].lower()
    nomes.append(name)
print(nomes)
print("\n")
find = False
while True:
    test = str(input("Enter whit the name: "))
    test = test[0].upper()+test[1:].lower()
    for x, e in enumerate(nomes):
        if test == e:
            print(e)
            print((x+1))
            find = True
            break
    else:
        print("Invalid Option!")

    if find:
        break
            
        

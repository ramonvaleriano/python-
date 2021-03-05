# Program: Algoritmo352_ProcuraNomePeloNome1.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 13:29
# Updated:

nomes = list()
quantity = 3
for e in range(quantity):
    name = str(input("Enter with the %d° name: " %(e+1)))
    name = name[0].upper()+name[1:].lower()
    nomes.append(name)
print(nomes)
print("\n")

test = str(input("Enter with the number: "))
test = test[0].upper()+test[1:].lower()

if test in nomes:
    print(test)
    number=nomes.index(test)
    print(number+1)
else:
    print("Invalid Opption")


# Program: Algoritmo351_ProcuraNomePeloNumero.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 13:01
# Updated:

nomes = list()
quantity = 5
for e in range(quantity):
    name = str(input("Enter with the %d° name: " %(e+1)))
    nomes.append(name)
print(nomes)
print("\n")
find = True
while find:
    test = int(input("Enter with a number: "))
    if test>0 and test<=quantity:
        print("The name: ", nomes[test-1])
        find = False
    else:
        print("Invalid Option!")
        
    

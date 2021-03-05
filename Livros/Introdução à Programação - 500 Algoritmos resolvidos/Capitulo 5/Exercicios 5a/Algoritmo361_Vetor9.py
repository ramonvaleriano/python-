# Program: Algoritmo361_Vetor9.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 19:23
# Updated:

generate = dict()
quantity = 3

for e in range(quantity):
    find = True
    data = list()
    while find:
        code = int(input("Enter with the code: "))
        name = str(input("Enter with the name: "))
        buy = float(input("Enter the value of the buy: "))
        if buy > 0:
            sale = float(input("Enter with the valeu of the sale: "))
            if sale >= buy:
                data.append(name)
                data.append(buy)
                data.append(sale)
                generate[code]=data
                find = False
            else:
                print("Invalid Option!")
        else:
            print("Invalid Option!")
print("\n\n")
test = int(input("Enter with the Code: "))
if test in generate:
    quantity = len(generate[test])
    for n in generate[test]:
        print(n)
else:
    print("Invalid Option!")
            
        

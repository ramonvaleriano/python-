# Program: Algoritmo358_Vetor6.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 17:46
# Updated:

store = list()
data = list()
products = 100
cont30 = 0
cont20 = 0
cont10 = 0

for e in range(products):
    cont=0
    while True:
        buy = float(input("Enter with the %d° buy: " %(e+1)))
        if buy >= 0:
            data.append(buy)
            sale = float(input("Enter with the valei of the sale: "))
            if sale > buy:
                data.append(sale)
                subtration = sale - buy
                converstion = (buy*100)/100
                converstion2 = (buy*20)/100
                if subtration < converstion:
                    cont10+=1
                if subtration >= converstion and subtration < converstion2:
                    cont20+=1
                if subtration >= converstion2:
                    cont30+=1
                break
            else:
                print("Invalid Value!")
        else:
            print("Invalid Value!")
    store.append(data)
print(cont10)
print(cont20)
print(cont30)

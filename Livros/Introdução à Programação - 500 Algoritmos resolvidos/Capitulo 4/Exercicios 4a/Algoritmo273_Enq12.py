# Program: Algoritmo273_Enq12.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 09:24
# Updated:

tax_1 = 0.3
tax_2 = 0.5
tax_3 = 0.7
cost_total = 0
cont_1 = 0
cont_2 = 0
cont1_2 = 0
costotal = 0
while True:
    number_consumer = int(input("Enter with your number of consumer: "))
    if number_consumer == 0:
        break
    quantity_kwh = float(input("Ebter with quantity: "))
    print("1 = Residencial")
    print("2 = Comercial")
    print("3 = Industrial")
    type_cosumer = int(input("Enter with the type: "))
    if  type_cosumer == 1:
        cost = quantity_kwh*tax_1
        cont_1+=1
        costotal+= cost
    elif type_cosumer == 2:
        cost = quantity_kwh*tax_2
        cont_2+=1
        costotal+= cost
    elif type_cosumer == 3:
        cost = quantity_kwh*tax_3
    print(cost)
    cost_total+=cost
    cont1_2 = cont_1 + cont_2
media1_2 = costotal/cont1_2
print(cost_total)
print(media1_2)

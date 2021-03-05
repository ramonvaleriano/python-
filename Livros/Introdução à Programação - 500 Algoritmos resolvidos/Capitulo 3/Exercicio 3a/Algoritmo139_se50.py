# Programa: Algoritmo139_se50.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 14:31
# Updated:

city = input("Enter with the name of the city: ")
quantity = int(input("Enter with quantity of the population: "))
candidate = int(input("Enter with quantity of the large: "))

test1 = type(quantity) is int
test2 = type(candidate) is int

tax = (quantity*50)/100

if(test1==True)and(test2==True)and(quantity>0)and(candidate>0):
    if(quantity >= 20000)and(candidate>=tax):
        print("Haverá segundo turno!")
    else:
        print("Não haverá segundo turno!")
else:
    print("Dou your crazy?")
print(city)

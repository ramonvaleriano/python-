# Program: Algoritmo307_Enq46.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 07/04/2020 - 08:37
# Updated:

tallest_man = 0
heavier_woman = 0
cont = 0
sum_age = 0

while True:
    test = "OK"
    name = input("Enter with your name: ")
    name = name.upper()
    if name == "@":
        break
    sex = input("Enter with your sex: ") # Male or Feminine
    sex = sex.upper()
    age = int(input("Enter with your age: "))
    weight = float(input("Enter with your weight: "))
    height =  float(input("Enter with your height: "))
    if sex == "MALE" and height>=tallest_man:
        tallest_man = height
        name_tallest_man = name
    elif sex == "FEMININE" and heavier_woman<=weight:
        heavier_woman = weight
        name_hearvier_woman = name
    else:
        test = "NOK"
        print("Invalid Option!")
        name_hearvier_woman = "Wrong"
        name_tallest_man = "wrong"

    if test == "OK":
        cont+=1
        sum_age+=age
    print()
    print(name)
    print(sex)
    print(age)
    print(weight)
    print(height)
    print()
print()
print(tallest_man)
print(name_tallest_man)
print()
print(heavier_woman)
print(name_hearvier_woman)

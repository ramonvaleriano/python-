# Program: Algoritmo190_para17.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 11:07
# Updated:

for e in range(20):
    name = input("Enter with your name: ")
    sex = input("Enter with your sex: ")
    sex = sex.upper()
    age = int(input("Enter with your age: "))
    if(sex == "MASCULINO")and(age>=21):
        print("\n%s\n" %name)
    print("\n")

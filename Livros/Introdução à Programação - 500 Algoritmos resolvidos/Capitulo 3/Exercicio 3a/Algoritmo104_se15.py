# Program: Algoritmo104_se15.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 24/03/2020 - 17:01
# Updated:

name = input("Enter with your name: ")
sex = input("Enter with your sex in portuguese: ")
age = int(input("Enter with your age: "))

if(((sex == "Feminino")or(sex == "FEMININO")or(sex == "feminino"))and(age<=25)):
    print("%s, Accept" %name)
else:
    print("Denied")

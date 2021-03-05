# Program: Exemplos_VideoAula11.py 
# Author: Ramon R. Valeriano
# Description: Exemplos de Video aula, DICIONÁRIO
# Developed: 28/04/2020 - 18:17
# Updated:

registro = dict()

name = str(input("Enter with your name: "))
date_birth = int(input("Enter wiht your year of birth: "))
if date_birth > 0 :
    work = int(input("Enter with the work card: "))
    registro["Name"] = name
    registro["Birth"] = date_birth
    registro["Work"] = work
    if work > 0:
        year = int(input("Year the firt work: "))
        new_date = year+25
        registro["New"]= new_date
        salary = float(input("Salary: "))
        age = int(input("Your age: "))
        new_age = age+25
        registro["Age"]=new_age
    else:
        work = 0
else:
    print("Invalid Option!")
for k, v in registro.items():
    print(f'{k} - {v}')

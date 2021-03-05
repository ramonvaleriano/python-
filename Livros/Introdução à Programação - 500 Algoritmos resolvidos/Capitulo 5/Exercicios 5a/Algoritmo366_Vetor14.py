# Program: Algoritmo366_Vetor14.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/04/2020 - 11:38
# Updated:

names_ = list()
professions = list()
quantity = 20
cont = 0
for e in range(quantity):
    name = str(input("Enter with the %d° name: " %(e+1)))
    name = name.upper()
    names_.append(name)
    profession = str(input("Enter with the %d° profession: " %(e+1)))
    profession =  profession.upper()
    professions.append(profession)
    if profession == "DENTISTA":
        cont+=1
        c_profession = profession
    else:
        c_profession = "DENTISTA"
    print("\n")
print("\n")

for n in range(quantity):
    print("%-12s - %-12s" %(names_[n],professions[n]))
if cont > 0:
    print("Total of %-12s: %d" %(c_profession, cont))
else:
    print("Do not hesitate: %-12s" %c_profession)

# Program: Algoritmo359_Vetor7.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 18:11
# Updated:

city = dict()
general = list()
people = 20

for e in range(people):
    date = list()
    while True:
        name = str(input("Enter with %d° name:" %(e+1)))
        name = name.upper()
        age = int(input("Enter with the %d° age: " %(e+1)))
        if age > 0:
            city[name]=age
            if name[0]=="S" or name[0]=="L":
                date.append(name)
                date.append(age)
                general.append(date)
            break
print("\n\n")
for k, v in city.items():
    print("%12s - %2d" %(k, v))
print("\n\n")
cont = 0
for n in general:
    print(n[cont], n[cont+1])
                
                
            
                
        
            

# Program: Algotimo216_Enq55.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 08/04/2020 - 11:44
# Updated:

cont_casado = 0
cont_viuvo = 0
cont_solteiro = 0
cont_separado = 0
cont_viuvo = 0 
sum_age = 0
cont_total = 0
while True:
    age = int(input("Enter with the your age: "))
    if age<=0:
        break
    marital_status = input("Enter with your marital status in Portuguese: ")
    marital_status = marital_status.upper()
    if marital_status == "CASADO":
        cont_casado+=1
        cont_total+=1
    elif marital_status == "SOLTEIRO":
        cont_solteiro+=1
        cont_total+=1
    elif marital_status == "SEPARADO":
        cont_separado+=1
        cont_total+=1
    elif marital_status == "VIUVO":
        cont_viuvo+=1
        sum_age+=age
        cont_total+=1
    else:
        print("Invalid Option!")
        
if cont_viuvo>0:
    media = sum_age/cont_total
else:
    media = 0
    
print(cont_casado)
print(cont_viuvo)
print(cont_solteiro)
print(cont_separado)
print(cont_viuvo)
print(media)

# Program: Algoritmo268_Enq7.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 11:29
# Updated:

cont_male = 0 
cont_feminine = 0

while True:
    sex = input("Enter with your sex in portuguese: ")
    sex = sex.upper()
    if sex == "FIM":
        break
    elif sex == "MASCULINO":
        cont_male+=1
print(cont_male)

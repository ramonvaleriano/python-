# Program: Algoritmo326_Enq64.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 20:11
# Updated:

cont_f = 0
cont_m = 0
higher_m = 0
supergirl = 0
sum_age = 0

while True:
    age = int(input("Enter with your age: "))
    if age <= 0 :
        break
    
    sex = input("Enter with your sex: ")
    sex = sex.upper()
    if sex == "FEMALE" and cont_f == 0:
        smaller = age
        
    experience = input("Enter if have experience/nY - Yes or N - Not: ")
    experience = experience.upper()
    
    if sex == "FEMALE":
        cont_f+=1
        if age <= 35 and experience == "Y":
            supergirl+=1
        if age < smaller:
            smaller = age
            
    elif sex == "MALE":
        if experience == "Y":
            cont_m+=1
            sum_age+=age
        if age >= 45:
            higher_m+=1
    else:
        print("Invalid Option!")
    
        
media_age_m = sum_age/cont_m
conversion_m = (higher_m*cont_m)/100
print(cont_f)
print(media_age_m)
print(conversion_m)
print(smaller)

# Program: Algoritmo247_Para74.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/202 - 08:14
# Updated:

higher = 30
current = 12
media_weight_tema = 0 
media_age_team = 0
cont_age_ = 0
cont_weight_ = 0

for e in range(higher):
    cont_age = 0
    cont_weight = 0
    country = input("Enter with the name your Country %02d: " %(e+1))
    for n in range(current):
        name = input("Enter with the %02d° name: " %(n+1))
        weight = float(input("Enter with the the %02d weight: " %(n+1)))
        age = int(input("Enter with the the %02d Height: " %(n+1)))
        cont_age+=age
        cont_weight+=weight
        
    cont_age_+=cont_age
    cont_weight_ =cont_weight
        
    media_age_team = cont_age/current
    media_weight_tema = cont_weight/current
    print()
    print(media_age_team)
    print(media_weight_tema)
totalage = cont_age_/higher
totalweight = cont_weight_/higher 
print()
print(totalage)
print(totalweight)

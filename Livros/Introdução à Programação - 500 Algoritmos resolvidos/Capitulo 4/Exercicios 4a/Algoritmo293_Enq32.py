# Program: Algoritmo293_Enq32.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/04/2020 - 09:20
# Updated:

cont = 0
sum_ = 0
cont_f = 0
cont_milf = 0
cont_m = 0
while True:
    age = int(input("Enter with your age: "))
    if age == 0:
        break
    sex = input("Enter with your sex: \nMale or Feminine: ")
    sex = sex.upper()
    cont+=1
    sum_+=age
    if sex == "FEMININE":
        cont_f+=1
        if ((age>=30)and(age<=45)):
            cont_milf+=1
    elif sex == "MALE":
        cont_m+=1
        
media = sum_/cont
print()
print(media)
print(cont_milf)
print(cont_m)
print()

# Programa: Algoritmo135_se46.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 13:38
# Updated:

age = int(input("Enter with the your age: "))

test = type(age) is int

if(test==True)and(age>0):
    if age<16:
        message = "Não é eleitor!"
    elif((age>=16)and(age<18)or(age>=65)):
        message = "Eleitor vonlutário!"
    else:
        message = "Eleitor Obrigatório!"
else:
    message = "What fuck is this?!"

print(message)

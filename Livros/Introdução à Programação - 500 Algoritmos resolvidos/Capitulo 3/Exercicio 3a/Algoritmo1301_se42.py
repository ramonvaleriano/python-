# Programa: Algoritmo1301_se42.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 12:10
# Updated:

name = input("Enter with the your name: ")

firt = name[0]
print(firt)

if(((firt>="a")or(firt>="A"))and((firt<="k")or(firt<="K"))):
    message = "Classroom 101."
elif(((firt>="l")or(firt>="L"))and((firt<="n")or(firt<="N"))):
    message = "Classroom 102."
elif(((firt>="o")or(firt>="O"))and((firt<="z")or(firt<="Z"))):
    message = "Classroom 103."
else:
    message= "What fuck is this?!"
print(message)

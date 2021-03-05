# Program: Algoritmo492_fun34.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 11/06/2020 - 09:58 
# Updated:

def verifica(lista):
    cont = (len(lista)-1)
    testando = "ok"
    while True:
        if cont == 0:
            break
        if(lista[cont]>lista[cont-1]):
            testando = True
        else:
            test = "nok"
            testando = False
        cont-=1
    if tesntado == "ok":
        return 1
    else:
        return 0

lista = list()

for e in range(10):
    number = int(input("Entre com um  número: "))
    lista.append(number)

print(verifica(lista))
    
            


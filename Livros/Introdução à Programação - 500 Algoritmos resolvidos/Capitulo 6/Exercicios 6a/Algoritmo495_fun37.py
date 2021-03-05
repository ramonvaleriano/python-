# Program: Algoritmo495_fun37.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 11/06/2020 - 11:45 
# Updated:

def crescente(lista):
    anterior = 0
    quantity = len(lista)
    while anterior<quantity:
        posterior = anterior+1
        while posterior<quantity:
            if(lista[anterior]>lista[posterior]):
                lista[anterior], lista[posterior] = lista[posterior], lista[anterior]
            posterior+=1
        anterior+=1
    return lista

nomes = list()
quantity = 10

for e in range(quantity):
    nome = str(input("Entre com %d nome: " %(e+1)))
    nomes.append(nome)

new_name = crescente(nomes)
for i in new_name:
    print(i)


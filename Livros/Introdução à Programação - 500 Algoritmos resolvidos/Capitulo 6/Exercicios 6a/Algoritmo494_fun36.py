# Program: Algoritmo494_fun36.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 11/06/2020 - 10:25 
# Updated:

def crescente(lista):
    anterior = 0
    quantity = len(lista)
    while anterior<quantity:
        posterior = anterior+1
        while posterior<quantity:
            if(lista[0][anterior]>lista[0][posterior]):
                lista[anterior], lista[posterior] = lista[posterior], lista[anterior]
            posterior+=1
        anterior+=1
    return lista

def mostrar(lista, funcao):
    new_lista = funcao(lista)
    for i in new_lista:
        print("%12s - %12s - %12s", %(i[0],i[0],i[2]))

agenda = list()
quantity = int(input("Digite quantas pessoas deseja armazenar: "))

for e in range(quantity):
    dados = list()
    nome = str(input("Entre com o nome da pessoa: "))
    endereco = str(input("Entre com o endereço dessa pessoa: "))
    profissao = str(input("Entre com o endereço dessa pessoa: "))
    dados.append(nome)
    dados.append(endereço)
    dados.append(profissao)
    agenda.append(dados[:])
print()
mostrar(lista, crescente)



# Program: Algoritmo386_Vetor34.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/05/2020 - 20:34
# Updated:

quantity = 2
agenda = dict()

for e in range(quantity):
    lista = list()
    name = str(input("Entre com o nome: "))
    name = name.upper()
    endereco = str(input("Entre com endereço: "))
    lista.append(endereco)
    phone = int(input("Entre com o número: "))
    lista.append(phone)
    agenda[name]=lista[:]
while True:
    print("Digite Finalizar de se desejar sair da agenda.")
    valor = str(input("Deseja dados de quem: "))
    valor = valor.upper()
    if valor == "FINALIZAR":
        break
    if valor in agenda:
        cont = 0
        for n in agenda.values():
            print(n[cont], end=" ")
            cont+=1
        print("\n\n")
    else:
        print("Não há essa pessoa na agenda!")
    
    

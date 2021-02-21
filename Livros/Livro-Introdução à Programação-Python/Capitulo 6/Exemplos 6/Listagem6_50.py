# Program: Listagem6_50.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 22/04/2020 - 22:57
# Updated:

tabela = { "Alface" : 0.45,
           "Batata" : 1.20,
           "Tomate" : 2.30,
           "Feijão" : 1.50 }
while True:
    alimento = input("Digite o alimento que deseja saber o valor: ")
    alimento = alimento[0].upper()+alimento[1:].lower()
    print(alimento, "\n\n")
    if alimento == "Fim":
        break
    elif(alimento in tabela):
        print(tabela[alimento])
    else:
        print("Alimento não existe na tabela!")

# Program: Algoritmo387_Vetor35.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/05/2020 - 21:17
# Updated:

classe = list()
quantity = 100

for e in range(quantity):
    dados = list()
    matricula = int(input("Entre com a matricula do aluno: "))
    dados.append(matricula)
    media = float(input("Entre com a media do aluno: "))
    dados.append(media)
    classe.append(dados[:])
maior = classe[0]
cont = 0 
for n in classe:
    if n[cont] > maior[1]:
        maior = n
print()
print(maior[0])
print(maior[1])
print()
print(classe)

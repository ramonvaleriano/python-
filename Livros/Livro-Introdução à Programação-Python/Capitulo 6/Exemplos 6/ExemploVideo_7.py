# Program: ExemploVideo_7.py
# Author: Ramon R. Valeriano
# Description: Exemplos de uma video aula que eu peguei na internet, sobre Dicionário
# Developed: 24/04/2020 - 23:58
# Updated:
estado = dict()
brasil = list()
for e in range(0, 3):
    estado["UF"]= str(input("Unidade Federa: "))
    estado["Sigla"]=str(input("Sigla:" ))
    brasil.append(estado.copy())
print()
for n in brasil:
    for k, v in estado.items():
        print(k, v)


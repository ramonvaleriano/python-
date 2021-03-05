# Program: Exemplos_VideoAula9.py 
# Author: Ramon R. Valeriano
# Description: Exemplos de Video aula, DICIONÁRIO
# Developed: 27/04/2020 - 23:00
# Updated:

estado = dict()
brasil = list()

for e in range(3):
    #estado= dict()
    estado["UF"]=str(input("Unidade Federativa: "))
    estado["Sigla"]=str(input("Sigla: "))
    brasil.append(estado.copy())
print(brasil)
print("\n")
for e in brasil:
    print(e["UF"],e["Sigla"] )
print("\n")
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')
print("\n")
for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print("\n")


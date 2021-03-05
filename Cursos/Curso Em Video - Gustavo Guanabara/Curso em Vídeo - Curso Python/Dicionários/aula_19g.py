# Program: aula_19g.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 06/10/2020 - 20:54

estado = dict()
brasil = list()

for c in range(3):
    estado = dict()
    estado['uf']=str(input('Unidade Federativa: ')).strip().upper()
    estado['sigla']=str(input('Sigla do Estado: ')).strip().upper()
    brasil.append(estado.copy())
print()
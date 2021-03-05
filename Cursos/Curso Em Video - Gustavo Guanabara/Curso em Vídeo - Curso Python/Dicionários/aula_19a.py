# Program: aula_19a.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 06/10/2020 - 16:35

dados = dict()

dados['Name']= 'Ramon'
dados['Sexo']= 'Masculino'
dados['Idade']= 31
dados['Palavrão']= 'Caralho'
print(dados)
del dados['Palavrão']
print(dados)
print(len(dados))
print(dados.items())
print(dados.keys())
print(dados.values())
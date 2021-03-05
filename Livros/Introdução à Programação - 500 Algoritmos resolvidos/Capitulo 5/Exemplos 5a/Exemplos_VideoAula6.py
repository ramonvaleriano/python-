# Program: Exemplos_VideoAula6.py
# Author: Ramon R. Valeriano
# Description: Exemplos de Video aula, DICIONÁRIO
# Developed: 27/04/2020 - 22:31
# Updated:

pessoas = dict()
pessoas = {"Nome":"Gustavo",
           "Sexo":"Masculino",
           "Idade":22}
print(pessoas)
print(pessoas["Nome"])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print("\n")
for k in pessoas.keys():
    print(k)
print("\n")
for v in pessoas.values():
    print(v)
print("\n")
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas["Sexo"]
print("\n")
for k, v in pessoas.items():
    print(f'{k} = {v}')
print("\n")
pessoas["Nome"]="Ramon"
for k, v in pessoas.items():
    print(f'{k} = {v}')
print("\n")
pessoas["Sexo"]="Macho Para o Caralho!"
for k, v in pessoas.items():
    print(f'{k} = {v}')
print("\n")
pessoas["Peso"]=80.89
for k, v in pessoas.items():
    print(f'{k} = {v}')
print("\n")

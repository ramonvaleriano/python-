# Program: ExemploVideo_5.py
# Author: Ramon R. Valeriano
# Description: Exemplos de uma video aula que eu peguei na internet, sobre Dicionário
# Developed: 24/04/2020 - 23:27
# Updated:

pessoas = {"Nome" :  "Ramon", "Sexo" : "Masculino", "Idade" : 30}
print(pessoas["Nome"])
print(pessoas["Idade"])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for e in pessoas.keys():
    print(e)
print()
for e in pessoas.values():
    print(e)
print()
for k, v in pessoas.items():
    print(k, v)
print()
del pessoas["Sexo"]
for k, v in pessoas.items():
    print(k, v)
print()
pessoas["Nome"] = "Milla"
for k, v in pessoas.items():
    print(k, v)
print()
pessoas["Peso"] = 80.79
for k, v in pessoas.items():
    print(k, v)
print()


 


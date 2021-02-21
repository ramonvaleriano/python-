# Program: ExemploVideo_1.py
# Author: Ramon R. Valeriano
# Description: Exemplos de uma video aula que eu peguei na internet, sobre Dicionário
# Developed: 24/04/2020 - 21:49
# Updated:

dados = dict()
dados = { "name" : "Pedro", "idade" : 25}
print(dados)
print(dados["name"])
print(dados["idade"])
dados["sexo"]="Masculino"
print(dados)
del dados["idade"]
print(dados)
test = dados.pop("sexo")
print(test)
print(dados)

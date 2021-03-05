# Program: Exemplos_VideoAula5.py
# Author: Ramon R. Valeriano
# Description: Exemplos de Video aula, DICIONÁRIO
# Developed: 27/04/2020 - 22:26
# Updated:

lista = list()

filme = {"Título":"Star Wars",
         "Ano":1977,
         "Diretor":"George Lucas"}
lista.append(filme)
filme = {"Título":"Avengers",
         "Ano":2012,
         "Diretor":"Joss Whendon"}
lista.append(filme)
filme = {"Título":"Matrix",
         "Ano":1999,
         "Diretor":"Wachowski"}
lista.append(filme)

print(lista)
print("\n\n")
print(lista[0]["Ano"])
print(lista[2]["Título"])

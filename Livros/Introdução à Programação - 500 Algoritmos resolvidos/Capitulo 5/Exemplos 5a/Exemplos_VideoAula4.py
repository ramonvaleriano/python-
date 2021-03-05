# Program: Exemplos_VideoAula4.py
# Author: Ramon R. Valeriano
# Description: Exemplos de Video aula, DICIONÁRIO
# Developed: 27/04/2020 - 22:19
# Updated:

filme = {"Título":"Star Wars",
         "Ano":1977,
         "Diretor":"George Lucas"}
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(k, v)

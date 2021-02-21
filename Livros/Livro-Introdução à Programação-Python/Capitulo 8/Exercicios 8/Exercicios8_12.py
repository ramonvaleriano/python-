# Program: Exercicios8_12.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 17:08
# Updated:

def pesquisa_nome(lista, nome):
    return nome in lista

lista = ["Ramon", 134, "Caralho", 398, "Porra", "Coisa chata"]
nome = str(input("Qual nome deseja procurar: "))
print(pesquisa_nome(lista, nome))
    

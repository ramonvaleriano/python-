# Program: Desafio1.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 13/09/2020 - 12:26

def coleta_dados():
    name = input("Digite o seu nome: ")
    return name

def mensage(i_name):
    print('Olá ',i_name)


name = coleta_dados()
mensage(name)

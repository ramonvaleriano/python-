# Program: Exercicios8_11.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 16:58
# Updated:

PERGUNTA = "Qual o nome que deseja validar: "

def nome_teste(PERGUNTA, maximo, minimo):
    while True:
        nome = str(input(PERGUNTA))
        quantity = len(nome)
        if quantity<minimo or quantity>maximo:
            print("Nome invalido!\n")
        else:
            return nome
minimo = int(input("Digite um valor minimo para entrada de dados: "))
maximo = int(input("Digite um valor máximo para entrada de dados: "))
print("\n\n")

nome_teste(PERGUNTA, maximo, minimo)

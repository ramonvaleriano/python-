# Program: Algoritmo490_fun32.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 11/06/2020 - 09:51 
# Updated:

def verifica(string, caracter):
    return(caracter in string)

def mensagem(teste, string, caracter):
    if(teste(string, caracter)):
        mensagem = "Esse caracter está aqui dentro."
        return mensagem
    else:
        mensagem = "Esse caracter não está aqui dentro!"
        return mesagem

def contando(teste, string, caracter):
    quantity = 0
    if(teste(string, caracter)):
        quantity = string.count(caracter)
        return quantity
    else:
        return quantity


def troca(teste, texto, string, conta, caracter1, caracter2="*"):
    if(teste(string, caracter1)):
        quantity = conta(teste, string, caracter1)
        mensagem = texto(teste, string, caracter1)
        trocando = string.replace(caracter1, caracter2)
        print(mensagem)
        print(trocando)
        print(quantity)
    else:
        mensagem = texto(teste, string, caracter1)
        print(mensagem)


        

nome = str(input("Digite um nome: "))
nome = nome.lower()
caracter1 = str(input("Digite o 1° caracater: "))
caracter1 = caracter1[0].lower()
print()
troca(verifica, mensagem, nome, contando, caracter1)


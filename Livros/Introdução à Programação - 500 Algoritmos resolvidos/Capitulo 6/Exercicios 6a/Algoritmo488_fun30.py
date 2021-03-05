# Program: Algoritmo488_fun30.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 11/06/2020 - 08:55 
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

def contando(teste, texto, string, caracter):
    if(teste(string, caracter)):
        quantity = string.count(caracter)
        print(texto(teste, string, caracter))
        print("{0} vezes que se repeti.".format(quantity))
    else:
        print(texto(teste, string, caracter))

nome = str(input("Digite um nome aqui: "))
nome = nome.lower()
caracter = str(input("Digite a letra que deseja procurar: "))
caracter = caracter[0].lower()
print()

contando(verifica, mensagem, nome, caracter)

        
        

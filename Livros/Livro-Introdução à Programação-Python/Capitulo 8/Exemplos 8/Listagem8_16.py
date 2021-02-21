# Program: Listagem8_16.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 16:41
# Updated:
pergunta = "Digite o valor desejado: "
def faixa(pergunta, maximo, minimo):
    while True:
        v = int(input(pergunta))
        if v<minimo or v>maximo:
            print("Valor Invalido.\nDigite Entre um valor %d e %d" %(minimo, maximo))
        else:
            return v
minimo = int(input("Digite um valor minimo para entrada de dados: "))
maximo = int(input("Digite um valor máximo para entrada de dados: "))
print("\n\n")
#numero = int(input("Digite o número desejado:"))

faixa(pergunta, maximo, minimo)

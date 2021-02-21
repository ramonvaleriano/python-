# Program: listagem8_16_Versao2.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 17/09/2020 - 06:38

def verificao(pergunta, minimo, maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print('Valor invalido! Digte na faixa {} e  {}'.format(minimo, maximo))
        else:
            return v

minimo = int(input("Digite o valor minimo: "))
maximo = int(input("Digite o valor maximo: "))

question = "Digite o valor desejado: "

print(verificao(question, minimo, maximo))
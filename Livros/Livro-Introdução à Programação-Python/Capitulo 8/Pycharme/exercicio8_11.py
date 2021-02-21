# Program: exercicio8_11.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 17/09/2020 - 06:47

def verifica(pergunta, minimo, maximo):
    while True:
        palavra = input(pergunta)
        quantidade = len(palavra)
        if(type(palavra)!='str'):
            print("Opção invalida! Digite apenas palavras com caracteres")
        elif quantidade<minimo or quantidade>maximo:
            print('Opção invalida! Digite uma palavra que {} e {} caracteres!'.format(minimo,maximo))
        else:
            return palavra

minimo = int(input('Digite a quantidade minima de carateres: '))
maximo = int(input('Digite a quantidade máxima de caracteres: '))

pergunta = 'Digite a palavra desejada: '

print(verifica(pergunta, minimo, maximo))
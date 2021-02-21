# Program: Exercicio6_9.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 20/04/2020 - 21:26
# Updated:

lista = [3,7,1,8,5,10, 25, 34]
number1 = int(input("Entre com o primeiro número a ser procurado: "))
number2 = int(input("Entre com o segundo número a ser procurado: "))
cont1 = 0
cont2 = 0
resposta1 = False
resposta2 = False
for e in lista:
    if e == number1:
        print("%d encontrado na posição %d" %(number1,cont1))
        resposta1 = True
    if e == number2:
        print("%d encontrado na posição %d" %(number2,cont2))
        resposta2 = True
    cont1+=1
    cont2+=1
if resposta1 or resposta2:
    if resposta1 and not resposta2:
        print("Apenas o número: %d foi encontrado!" %number1)
    elif resposta2 and not resposta1:
        print("Apenas o número: %d foi encontrado!" %number2)
    elif resposta1 and resposta2:
        print("Os dois numeros %d e %d foram encontrados." %(number1, number2))
        if cont1<cont2:
            first = number1
            print("O primeiro número a ser encontrado: %d" %first)
        else:
            first = number2
            print("O primeiro número a ser encontrado: %d" %first)
    else:
        print("Opção Invalida!")
else:
    print("Não há nenhum dos dois número nessa lista!")

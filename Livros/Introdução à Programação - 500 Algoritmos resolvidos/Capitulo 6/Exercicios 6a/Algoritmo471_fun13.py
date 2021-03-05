# Program: Algoritmo471_fun13.py
# Author: Ramon R. Valerino
# Description:
# Developed: 08/06/2020 - 11:16
# Updated:

def verifica(number1, number2):
    return(number1%number2==0)

def quantidade(number1, number2, funcao):
    cont = 0
    if funcao(number1, number2):
        while funcao(number1, number2):
            result=number1/number2
            number1 = result
            cont+=1
    return cont

def exibir(number1, number2, funcao1, funcao2):
    if funcao1(number1, number2):
        print("Os números são divisiveis!")
        print("Quantidade = %d" %funcao2(number1, number2, funcao1))
    else:
        print("Os número não são divisiveis!")


numero1 = int(input("Digite o número que você deseja verrificar se é divisivel: "))
numero2 = int(input("Digite o número que irá dividir: "))

exibir(numero1, numero2, verifica, quantidade)


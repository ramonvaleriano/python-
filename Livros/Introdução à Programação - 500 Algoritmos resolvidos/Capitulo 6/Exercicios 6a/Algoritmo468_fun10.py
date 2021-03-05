# Program: Algoritmo468_fun10.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 08/06/2020 - 10:09
# Updated:

def positivo(number):
    reuslt = 0
    (result=number) if number>=0 else (result = (number*-1))
    return result

def test_indice(number):
    result = number if number>=2 else result = 2

def calculo(number, root, funcao1, funcao2):
    radicando = funcao1(number)
    indice = funcao2(root)
    result = radicando**indice
    return result

for e in range(3):
    numero = float(input("Entre com o número que deseja obeter a raiz: "))
    raiz = float(input("Digite o número que será o indicie dessa raiz: "))
    resultado = calculo(numero, raiz, positivo, test_indice)
    print(resultado)
    print()

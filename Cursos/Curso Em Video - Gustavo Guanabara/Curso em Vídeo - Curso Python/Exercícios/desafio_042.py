# Program: desafio_042.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 19:03

lado1 = float(input('Digite o Primeiro lado do triângulo: '))
lado2 = float(input('Digite o Segundo lado do triângulo: '))
lado3 = float(input('Digite o Terceiro lado do triângulo: '))

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado2 + lado1):
    if (lado1!=lado2)and(lado1!=lado3)and(lado3!=lado2):
        print('Triângulo Ecaleno!')
    elif(((lado1==lado2)and(lado1!=lado3))or((lado1==lado3)and(lado1!=lado2))or
         ((lado2==lado3)and(lado2!=lado1))):
        print('Triangulo Isósceles!')
    else:
        print('Triângulo Equilátero!')
else:
    print('Não pode ser um triângulo!')
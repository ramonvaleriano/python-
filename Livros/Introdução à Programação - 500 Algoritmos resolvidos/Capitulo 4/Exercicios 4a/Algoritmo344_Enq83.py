# Program: Algoritmo344_Enq83.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/04/2020 - 21:14
# Updated:

import math

while True:
    print("X"+"-"*50+"x")
    print("X"+"-"*23+"MENU"+"-"*23+"x")
    print("A - Entrar com um frase e armazenar em outra variável")
    print("    a frase invertida e imprimir")
    print("B - Entrar com um número e o seu número de digitos e ")
    print("    Imprimir invertido")
    print("C - Calcula e imprime a tangente de um angulo em")
    print("    graus. ")
    print("F - Sair do Programa.")
    option = input("OPÇÃO: ")
    option = option.upper()
    print("X"+"-"*50+"x")
    print("X"+"-"*50+"x")
    print("\n\n")

    cont = 0
    cont1 = 0
    
    if option == "F":
          break
        
    elif option == "A":
        name = input("Entre com o° nome: ")
        quantity = len(name)
        list1 = []
        for e in range(quantity-1, -1, -1):
            test = name[e]
            list1.append(test)
            
        print("O nome invertido é:")
        print("%s" %list1)
        print("\n\n")

    elif option == "B":
        name = input("Entre com um nome: ")
        quantity = len(name)
        for n in range(quantity, -1, -1):
            for g in range(n):
                print(name[g], end=" ")
            print()
        print("\n")

    elif option == "C":
        number = float(input("Entre com um número em graus: "))
        result = math.tan(number)
        print("O rsultado é: %7.3f" %result)
        print("\n\n")

    else:
        print("Opção Invalida!")
            
    
            
              
          

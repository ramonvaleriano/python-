# Program: Algoritmo343_Enq82.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/04/2020 - 20:28
# Updated:

import math

while True:
    print("X"+"-"*50+"x")
    print("X"+"-"*23+"MENU"+"-"*23+"x")
    print("A - Armazena na variável menor e imprime o nome que")
    print("    tive o menor número.")
    print("B - Brinca com a palavra.")
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
        name = input("Entre com o %d° nome:" %(cont+1))
        smaller = len(name)
        for e in range(2):
            cont+=1
            test1 = 0
            name = input("Entre com o %d° nome:" %(cont+1))
            test1 = len(name)
            if test1 < smaller:
                smallest_name = name[:]
        print("O menor nome é:")
        print("%s" %smallest_name)
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
            
    
            
              
          

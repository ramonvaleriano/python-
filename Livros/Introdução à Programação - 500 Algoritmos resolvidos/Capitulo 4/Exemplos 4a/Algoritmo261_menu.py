# Program: Algoritmo261_menu.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 10:20
# Updated:

while True:
    print("X"+"-"*42+"X")
    print("X"+"-"*19+"MENU"+"-"*19+"X")
    print("Options: ")
    print("A -  Armazena na varável menor e imprime")
    print("o nome que tiver menor número de de cara-")
    print("cteres entre três")
    print("B - Gera e Imprime uma nova Palavra")
    print("C - Calcula e Imprime a Raiz a quarta de um")
    print("número")
    print("F - Finalizar")
    option = input("\nOption: ")
    print("X"+"-"*42+"X")
    print("X"+"-"*42+"X")
    print("\n")
    option = option.upper() # Todas letras em Mausculo
    test = option[0] # Garente apenas o 1° Caracter
#x-------------------------------------------------------X
#x------------Começa a Condição F------------------------X
    if test == "F": 
        break #Finaliza while, o programa!
#x-------------------------------------------------------X
#x------------Começa a Condição A------------------------X
    elif test == "A":
        for e in range(3):
            name = input("Enter with %d° name: "%(e+1))
            smaller = name[:]
            quantity_name = len(name)
            quantity_smaller = len(smaller)
            if quantity_smaller <= quantity_name:
                smaller = name[:]
        print("\n")
        print("X"+"-"*42+"X")
        print(smaller)
        print("X"+"-"*42+"X")
        print("\n")
#x-------------------------------------------------------X
#x------------Começa a Condição B------------------------X
    elif test == "B":
        word = input("Enter with a word: ")
        print("\n")
        print("X"+"-"*42+"X")
        print(word)
        print("X"+"-"*42+"X")
        print("\n")
#x-------------------------------------------------------X
#x------------Começa a Condição c------------------------X
    elif test == "C":
        number = float(input("Enter with a number: "))
        if number>=0:
            result = number**(1/4)
        else:
            print("Invalid Number!")
            result = 0 
        print("\n")
        print("X"+"-"*42+"X")
        print(result)
        print("X"+"-"*42+"X")
        print("\n")
#x-------------------------------------------------------X
#x------------Opção Invalida, WRONG----------------------X
    else:
        message = "Invalid Option!"
        print("\n")
        print("X"+"-"*42+"X")
        print(message)
        print("X"+"-"*42+"X")
        print("\n")

        
print("\n\nPrograma Finalizado!\n")

# Program: Algoritmo342_Enq81.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/04/2020 - 19:14
# Updated:

while True:
    print("X"+"-"*50+"x")
    print("A - Imprime o nome que tiver o maior numero de")
    print("    de caracteres entre 20 nomes.")
    print("B - Brinca com a palavra.")
    print("C - Calcula e imprime a raiz à quarta de um número.")
    print("F - Termina o programa.")
    option = input("OPÇÃO:  ")
    option = option.upper()
    print("X"+"-"*50+"x")
    print("\n\n")

    bigger = 0
    quantity = 200
    test3 = "NOK"
    
    if option == "F":
        break
    
    elif option == "A":
        for e in range(quantity):
            test = 0
            name = input("Digite o %d° nome: " %(e+1))
            test = len(name)
            if test>bigger:
                biggest_name = name[:]
        print("O maior nome é:")
        print("%s" %biggest_name)
        print("\n\n")

    elif option == "B":
        name = input("Entre com um nome: ")
        test1 = len(name)
        for n in range(test1):
            for g in range(n+1):
                print(name[g],end=" ")
            print()
        print("\n\n")
    elif option == "C":
        while test3 != "OK":
            number = float(input("Entre com um número qualquer: "))
            if number >= 0:
                root = number**(1/4)
                print("A raiz a quarta desse número é:")
                print("%7.3f" %root)
                print("\n\n")
                test3 = "OK"
            else:
                print("Número invalido!")
                print("Repita a operação.")
                print()
    else:
        print("Opção Invalida!")
        print("\n\n")
            
        
    
    

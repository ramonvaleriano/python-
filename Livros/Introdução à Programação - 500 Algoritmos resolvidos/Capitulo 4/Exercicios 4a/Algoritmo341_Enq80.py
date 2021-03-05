# Program: Algoritmo341_Enq80.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/04/2020 - 18:49
# Updated:

while True:
    print("X"+"-"*30+"x")
    print("Maquina Esperta")
    print("1 - Soma varios números ")
    print("2 - Multiplica varios números ")
    print("3 - Sai do programa")
    option = int(input("OPÇÃO:  "))
    print("X"+"-"*30+"x")
    
    cont = 0
    sum_ = 0
    multiplication = 1
    
    if option == 3:
        break
    
    elif option == 1:
        while True:
            number = float(input("Entre com o %d° número: " %(cont+1)))
            print("Deseja somar mais um número:")
            print("S - Sim\nN - Não")
            answer = input("Resposta:  ")
            answer = answer.upper()
            if answer == "N":
                print("\nA soma = %6.3f\n" %sum_)
                break
            elif answer == "S":
                sum_+=number
            else:
                print("Opção Invalida!")
            print("\nA soma = %6.3f\n" %sum_)
            cont+=1
            
    elif option == 2:
        while True:
            number = float(input("Entre com o %d° número: " %(cont+1)))
            print("Deseja multiplicar mais um número:")
            print("S - Sim\nN - Não")
            answer = input("Resposta:  ")
            answer = answer.upper()
            if answer == "N":
                print("\nA multiplicação = %6.3f\n" %multiplication)
                break
            elif answer == "S":
                multiplication*=number
            else:
                print("Opção Invalida!")
            print("\nA multiplicação = %6.3f\n" %multiplication)
            cont+=1
    else:
        print("Opção Invalida!")

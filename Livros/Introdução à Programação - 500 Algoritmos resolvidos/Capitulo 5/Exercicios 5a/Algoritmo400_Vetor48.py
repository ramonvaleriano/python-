# Program: Algoritmo400_Vetor48.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 12/05/2020 - 21:10
# Updated:

hotel = list()
cont = 0
quantity = 50
while True:
    quarto = list()
    print("-"*54)
    print("-"*20+"Hotel Fazenda "+"-"*20)
    print("-"*54)
    print("1 - Cadatrar Quartos")
    print("2 - Listar Todos os quartos.")
    print("3 - Lista de quartos ocupados.")
    print("4 - Alugue/Reserva de Quarto.")
    print("5 - Entra despesas extras.")
    print("6 - Calcula despesa do quarto.")
    print("7 - Sair")
    print("-"*54)
    option = int(input("Digite a Opção desejada: "))
    print("-"*54)
    print("-"*54)
    print("\n\n")
    if option == 7:
        print("-"*54)
        print("Programa Finalizado.")
        print("-"*54)
        break
    elif option == 1:
        if cont<quantity:
            print("-"*54)
            number = int(input("Digite o número do quarto a ser adicionado: "))
            if number>0:
                value = float(input("Digite o valor da diaria do quarto: "))
                if value>0:
                    quarto.append(number)
                    quarto.append(value)
                    cont+=1
                    print("-"*54)
                    print("\n\n")
                else:
                    print("Opção Invalida para um quarto!")
                    print("-"*54)
                    print("\n\n")
            else:
                print("Opção Invalida para um quarto!")
                print("-"*54)
                print("\n\n")
        else:
            print("Número máximo de quartos atingidos!")
            print("-"*54)
            print("\n\n")
            

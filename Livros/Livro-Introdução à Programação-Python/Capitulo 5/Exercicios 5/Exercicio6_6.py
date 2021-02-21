# Program: Exercicio6_6.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 12:22
# Updated:

#X--------------------------Dados para fila 1-------------------------------------------X#

ultimo1 = 10
fila1 = list(range(1, ultimo1+1))

#X--------------------------Dados para fila 2-------------------------------------------X#

ultimo2 = 10
fila2 = list(range(1, ultimo2+1))


while True:
    print("\n")
    print("\nExistem %d clientes na fila 1." %len(fila1))
    print("Fila atual: ", fila1)
    print("\n")
    print("\nExistem %d clientes na fila 2." %len(fila2))
    print("Fila atual: ", fila2)
    print("\n")
    print("Digete G para trabalhar com a fila 1." )
    print("ou digite B para trabalhar com a fila 2.")
    print("Digete F para Adicionar um Cliente ao fim da fila: ")
    print("ou A para realizar um Atendimento. S para Sair: ")
    tipo = input("Operação G ou B: ")
    tipo = tipo.upper()
    operacao1 = input("Operação F, A ou S: ")
    operacao1 = operacao1.upper()
    if tipo == "G": #x-----------------Começa aqui a trabalhar coma a Fila 1------------X#
        if operacao1 == "A":
            if len(fila1)>0:
                atendido1 = fila1.pop(0)
                print("Cliente %d atendido na Fila 1." %atendido1)
            else:
                print("Fila vazia! Ninguém para atender na Fila 1.")
        elif operacao1 == "F":
            ultimo1+=1
            fila1.append(ultimo1)
        elif operacao1 == "S":
            break
        else:
            print("Operação Invalida! Digite apenas A, F ou S")
    elif tipo =="B": #x-----------------Começa aqui a trabalhar coma a Fila 2------------X#
        if operacao1 == "A":
            if len(fila2)>0:
                atendido2 = fila2.pop(0)
                print("Cliente %d atendido na Fila 1." %atendido2)
            else:
                print("Fila vazia! Ninguém para atender na Fila 1.")
        elif operacao1 == "F":
            ultimo2+=1
            fila1.append(ultimo2)
        elif operacao1 == "S":
            break
        else:
            print("Operação Invalida! Digite apenas A, F ou S")
    else:
        print("\n\nTipo de Fila invalida! Digite Apenas G ou B para selecionar as filas.\n\n")
        

#----------------------------------------------------------------------------------------#
        
        
    

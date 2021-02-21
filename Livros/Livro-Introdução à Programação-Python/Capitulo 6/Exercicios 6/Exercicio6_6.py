# Program: Exercicio6_6.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 20/04/2020 - 20:38
# Updated:

ultimo1 = 10
fila1 = list(range(1, ultimo1+1))
ultimo2 = 10
fila2 = list(range(1, ultimo2+1))

option = True

while True:
    print("\nExitem %d clientes na fila 1" %len(fila1))
    print("Fila atual:", fila1)
    print("\nExitem %d clientes na fila 2" %len(fila2))
    print("Fila atual:", fila2)
    print("\n")
    print("Em qual das filas deseja trabalhar:")
    print("Digite 1 para fila 1. 2 para fila 2. 3 para Sair do Pograma.")
    decisao = int(input("Decisão: "))
    if decisao == 3:
        break
    elif decisao == 1:
        print("Digite F para Adcionar um cliente ao fim da fila 1,")
        print("ou A para realizar o atendimentona fila 1. S para sair.")
        operacao = input("Operação(F, A ou S):  ")
        operacao = operacao.upper()
        quantidade = len(operacao)
        cont = 0
        while cont<quantidade:
            if operacao[cont] == "A":
                if (len(fila1))>0:
                    atendimento = fila1.pop(0)
                    print("Cliente %d atendido" %atendimento)
                else:
                    print("Fila Vazia! Ninguém para atender.")
            elif operacao[cont] == "F":
                ultimo1+=1 #Incrementa o ticket do novo cliente
                fila1.append(ultimo1)
            elif operacao[cont] == "S":
                option = False
                break
            else:
                print("Operação Invalida! Digite apenas F, A ou S!")
            cont+=1
    elif decisao == 2:
        print("Digite F para Adcionar um cliente ao fim da fila 1,")
        print("ou A para realizar o atendimentona fila 1. S para sair.")
        operacao = input("Operação(F, A ou S):  ")
        operacao = operacao.upper()
        quantidade = len(operacao)
        cont = 0
        while cont<quantidade:
            if operacao[cont] == "A":
                if (len(fila2))>0:
                    atendimento = fila2.pop(0)
                    print("Cliente %d atendido" %atendimento)
                else:
                    print("Fila Vazia! Ninguém para atender.")
            elif operacao[cont] == "F":
                ultimo2+=1 #Incrementa o ticket do novo cliente
                fila2.append(ultimo2)
            elif operacao[cont] == "S":
                option = False
                break
            else:
                print("Operação Invalida! Digite apenas F, A ou S!")
            cont+=1
    else:
        print("Operação Invalida!")
        
    

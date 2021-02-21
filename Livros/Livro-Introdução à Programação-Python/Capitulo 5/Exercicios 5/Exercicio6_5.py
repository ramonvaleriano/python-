# Program: Exercicio6_5.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 11:37
# Updated:

ultimo = 10
fila = list(range(1, ultimo+1))
cont = 0
test1 = 0
while True:
    if test1 == "OK":
        break
    print("\nExistem %d clientes na fila." %len(fila))
    print("Fila atual: ", fila)
    print("Digete F para Adicionar um Cliente ao fim da fila: ")
    print("ou A para realizar um Atendimento. S para Sair: ")
    operacao = input("Operação F, A ou S: ")
    quantity = len(operacao)
    if quantity>1:
        while cont<quantity:
            test = operacao[cont]
            test = test.upper()
            if test == "A":
                if((len(fila))>0):
                    atendido = fila.pop(0)
                    print("Cliente %d atendido." %atendido)
                else:
                    print("Fila vazia! Ninguém para atender.")
            elif test == "F":
                ultimo+=1 #Incrementa o ticjet do novo cliente.
                fila.append(ultimo)
            elif test == "S":
                test1="OK"
                break
            else:
                print("Operação Invalida! Digite apenas A, F ou S")
            cont+=1
    else:       
        operacao = operacao.upper()
        if operacao == "A":
            if((len(fila))>0):
                atendido = fila.pop(0)
                print("Cliente %d atendido." %atendido)
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao=="F":
            ultimo+=1 #Incrementa o ticjet do novo cliente.
            fila.append(ultimo)
        elif operacao=="S":
            break
        else:
            print("Operação Invalida! Digite apenas A, F ou S")
print("\n\n", fila, "\n\n")

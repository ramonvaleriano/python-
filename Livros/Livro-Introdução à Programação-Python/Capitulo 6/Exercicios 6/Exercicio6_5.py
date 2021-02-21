# Program: Exercicio6_5.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 20/04/2020 - 20:08
# Updated:

ultimo = 10
fila = list(range(1, ultimo+1))
option = True
while True:
    print("\nExitem %d clientes na fila" %len(fila))
    print("Fila atual:", fila)
    if not option:
        print("Fim do Programa!")
        break
    print("Digite F para Adcionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação(F, A ou S):  ")
    operacao = operacao.upper()
    quantidade = len(operacao)
    cont = 0
    while cont<quantidade:
        if operacao[cont] == "A":
            if (len(fila))>0:
                atendimento = fila.pop(0)
                print("Cliente %d atendido" %atendimento)
            else:
                print("Fila Vazia! Ninguém para atender.")
        elif operacao[cont] == "F":
            ultimo+=1 #Incrementa o ticket do novo cliente
            fila.append(ultimo)
        elif operacao[cont] == "S":
            option = False
            break
        else:
            print("Operação Invalida! Digite apenas F, A ou S!")
        cont+=1
    

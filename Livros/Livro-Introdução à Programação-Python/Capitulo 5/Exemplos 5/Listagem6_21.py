# Program: Listagem6_21.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 11:37
# Updated:

ultimo = 10
fila = list(range(1, ultimo+1))

while True:
    print("\nExistem %d clientes na fila." %len(fila))
    print("Fila atual: ", fila)
    print("Digete F para Adicionar um Cliente ao fim da fila: ")
    print("ou A para realizar um Atendimento. S para Sair: ")
    operacao = input("Operação F, A ou S: ")
    operacao = operacao.upper()
    if operacao == "A":
        if((len(fila))>0):
            atendido = fila.pop(0)
            print("Cliente %d atendido." %atendido)
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operacao=="F":
        ultimo+=1 #Incrementa o ticjet do novo cliente.
    elif operacao=="S":
        break
    else:
        print("Operação Invalida! Digite apenas A, F ou S")
#print(fila)

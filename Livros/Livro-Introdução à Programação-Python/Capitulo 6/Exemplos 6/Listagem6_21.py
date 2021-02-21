# Program: Listagem6_21.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 20/04/2020 - 19:46
# Updated:

ultimo = 10
fila = list(range(1, ultimo+1))
while True:
    print("\nExitem %d clientes na fila" %len(fila))
    print("Fila atual:", fila)
    print("Digite F para Adcionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação(F, A ou S):")
    operacao = operacao.upper()
    if operacao == "A":
        if (len(fila))>0:
            atendimento = fila.pop(0)
            print("Cliente %d atendido" %atendimento)
        else:
            print("Fila Vazia! Ninguém para atender.")
    elif operacao == "F":
        ultimo+=1 #Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação Invalida! Digite apenas F, A ou S!")
    

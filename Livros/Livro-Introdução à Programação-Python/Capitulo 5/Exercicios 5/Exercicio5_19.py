# Program: Exercicio5_19.py 
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 09:58
# Updated:

valor = float(input("Digite o valor a se pagar: "))
rest = valor - int(valor)
valor = int(valor)
cedulas = 0
atual = 100
apagar = valor
while True:
    if atual<=apagar:
        apagar-=atual
        cedulas+=1
    else:
        print("%d Cédulas de R$%d" %(cedulas, atual))
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0

if rest > 0:
    cedulas = 0
    atual = 0.50
    apagar = rest
    while True:
        if atual<=apagar:
            apagar-=atual
            cedulas+=1
        else:
            print("%d Cédulas de R$%f" %(cedulas, atual))
            if apagar == 0.00:
                break
            if atual == 0.50:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.02
            elif atual == 0.02:
                atual = 0.01
            cedulas = 0
    
    
        
        

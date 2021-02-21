# Program: Listagem6_35.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 21/04/2020 - 12:24
# Updated:

lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Sala (0 para sair): "))
    if sala == 0:
        print("Fim!")
        break
    if sala>len(lugares_vagos) or sala<1:
        print("Sala Invalida!")
    elif lugares_vagos[sala-0]==0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input("Quantos lugares você deseja (%d Vagos): "
                            % lugares_vagos[sala-1]))
        if lugares > lugares_vagos[sala-1]:
            print("Um número de lugares não está disponível!")
        elif lugares < 0:
            print("Número invalido!")
        else:
            lugares_vagos[sala-1]-=lugares
            print("%d lugares vendidos." %lugares )
    print("Utilização das salas.")
for x, l in enumerate(lugares_vagos):
    print("Sala %d - %d lugar(es) vazio(s)" %((x+1), l)) 
        

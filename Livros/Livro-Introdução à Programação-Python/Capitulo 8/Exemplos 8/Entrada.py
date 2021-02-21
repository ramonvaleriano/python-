# Program: Entrada.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 19:53
# Updated:

def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= minimo and v <= maximo:
                return v
            else:
                print("Digite um número entre %d e %d" %(minimo, maximo))
        except:
            print("Você deve digitar um número inteiro!")


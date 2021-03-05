# Program: aula_21l.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 08/10/2020 - 13:23

def par_impar(num=0):
    if num%2==0:
        return True
    else:
        return False

def resposta(test):
    resposta_ = test
    if resposta_:
        return 'É par!'
    else:
        return 'É impar!'

number = int(input('Digite um número: '))
print(resposta(par_impar(number)))
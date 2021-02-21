# Program: Exercicio5_27.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 30/03/2020 - 12:38
# Updated:

test = input("Digite o número desejado: ")
i = 0
f = len(test) - 1
while f > i and test[i]==test[f]:
    f-=1
    i+=1
if test[i]==test[f]:
    print("É um políndromo!")
else:
    print("Não é um políndromo!")


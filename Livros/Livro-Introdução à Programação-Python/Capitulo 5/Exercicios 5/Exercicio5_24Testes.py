# Program: Exercicio5_24Testes.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 30/03/2020 - 11:53
# Updated:

number = int(input("Digite o número para ser testado: "))
cont_number=1
cont = 0
while cont_number<=number:
    result = number%cont_number
    if result==0:
        cont+=1
    #print(cont_number)
    cont_number+=1
if cont == 2:
    message = "Esse número é primo!"
else:
    message = "Esse número não é primo!"
print(message)

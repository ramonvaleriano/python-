# Program: Exercicio5_23Testes.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 30/03/2020 - 12:01
# Updated:

number = int(input("Digite o número para ser testado: "))
cont_number=1
#cont = 0
while cont_number<=number:
    cont = 0
    number_test = 1
    while number_test<=cont_number:
        result=cont_number%number_test
        if result == 0:
            cont+=1
        number_test+=1
    if cont == 2:    
        print(cont_number)
    cont_number+=1

# Program: Algoritmo300_Enq39.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 08:48
# Updated:

cont_flum = 0
cont_botaf = 0
cont_vasco = 0
cont_flamerda = 0
cont_outros = 0
sum_salary = 0
cont_Rj_outros = 0
cont_Nit_Flum = 0

while True:
    print("X"+"-"*30+"X")
    print("Qual seu time do coração? ")
    print("1 - Fluminence")
    print("2 - Botafogo")
    print("3 - Vasco")
    print("4 - Flamengo")
    print("5 - Outros")
    option = int(input("Enter with the option: "))
    print("X"+"-"*20+"X")
    if option == 0:
        break
    elif (type(option) is int)and((option>=1)and(option<=5)):
        if option == 1:
            cont_flum+=1
        if option == 2 :
            cont_botaf+=1
        if option == 3 :
            cont_vasco+=1
        if option == 4 :
            cont_flamerda+=1
        if option == 5 :
            cont_outros+=1
        print("Where do you live: ")
        print("1 - RJ")
        print("2 - Niteroi")
        print("3 - Outros")
        option2 = int(input("Enter with the option: "))
        print("X"+"-"*20+"X")
        salary = float(input("What is your salary: "))
        print("X"+"-"*30+"X")
        
        if (type(option2) is int)and((option2>=1)and(option2<=3)):
            if option == 2:
                sum_salary+=salary
            elif option2 == 1 and option == 5:
                cont_Rj_outros+=1
            elif option2 == 2 and option == 1:
                cont_Nit_Flum+=1    
        else:
            print("Invalid Option!")        
        
    else:
        print("Invalid Option!")
media_botafogo = sum_salary/cont_botaf
print("The quantity Fluminence %d." %cont_flum)
print("The quantity Botafogo %d." %cont_botaf)
print("The quantity Vasco %d." %cont_vesco)
print("The quantity Flamengo %d." %cont_flamerda)
print("The quantity Outros %d." %cont_outros)
print("The media salary botafogo %d." %media_botafogo)
print("The quantity RJ %d." %cont_Rj_outros)
print("The quantity Niteroi %d." %cont_Nit_Flum)


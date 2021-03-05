# Program: Algoritmo360_Vetor8.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 18:37
# Updated:

signos = [[1, 20, "Capricórnio"],
         [2, 19, "Aquário"],
         [3, 20, "Peixes"],
         [4, 20, "Áries"],
         [5, 20, "Touro"],
         [6, 20, "Gêmeos"],
         [7, 21, "Câncer"],
         [8, 22, "Leão"],
         [9, 22, "Virgem"],
         [10, 22, "Libra"],
         [11, 21, "Escorpião"],
         [12, 21, "sagitário"]]
quantity = 12
while True:
    birth = int(input("Enter with the date of brith on the format: ddmmaaaa -> "))
    if birth == 9999:
        break
    if birth >= 10000000 and birth <= 99999999:
        day = int(birth/1000000)
        month = int((birth%1000000)/10000)
        year = int(birth%10000)
        print(day, month, year)
        if(((day<=31)and(day>=1))and((month>=1)and(month<=12))and((year>0)and(year<=9999))):
            for e in range(12):
                if month == signos[e][0]:
                    if day <= signos[e][1]:
                        print(signos[e][2])
                    else:
                        print(signos[e+1][2])
        else:
            print("Invalid Option!")
                    
        
    

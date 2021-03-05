# Program: Algoritmo369_Vetir17.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 27/04/2020 - 18:29 
# Updated:

tables = list(range(100,130))
chairs = list(range(5))
dict_tables = dict()
cont = 0
for e in tables:
    dict_tables[e]=chairs[:] # Se não for dessa forma, fazendo uma copia
                             # irá dar problema, ele irá copiar a referência 
                             # e não os dados em si.
while cont<150:
    disponibles = list(dict_tables.keys())
    print("The disponibles tables: ")
    print(disponibles, end=" ")
    print("\n")
    reservetion = int(input("Enter with the table number: "))
    if(reservetion in dict_tables):
        places = dict_tables[reservetion]
        quantity_chairs = len(places)
        if quantity_chairs > 0:
            print("\n")
            print("The chairs: ")
            print(places)
            print("\n")
            chose = int(input("How manu charis do you want: "))
            quantity_chairs = len(places) 
            if chose <= quantity_chairs:
                del dict_tables[reservetion][:chose]
                print(dict_tables[reservetion])
                print("\n")
                cont+=chose
                print("\n\n%d\n\n" %cont)
                if len(dict_tables[reservetion]) == 0:
                    del dict_tables[reservetion]
                #dict_tables = dict_tables.copy()
            else:
                print("Invalid Option!")
        else:
            print("Invalid Option!")
    else:
        print("Invalid Option!")
        

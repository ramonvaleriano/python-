# Program: Algoritmo370_Vetor18.py 
# Author: Ramon R. Valeriano
# Description: 
# Developed: 28/04/2020 - 19:20
# Updated:

company = list()

while True:
    flight = list()
    chair = list()
    flight_number = int(input("Enter with the flight number: "))
    if flight_number <= 0:
        break
    flight.append(flight_number) 
    quantity = int(input("Enter with the number chair: "))
    if quantity > 0:
        chair = list(range(quantity))
        flight.append(chair[:])
    else:
        chair = list()
        flight.append(chair[:])
    company.append(flight[:])
#print(company)
while True:
    for i in company:
        print(i[0], i[1])
    print("\n")
    register = int(input("Enter with your resgister card: "))
    if register <=0:
        break
    else:
        number = int(input("Enter with the flight number: "))
        testando = True
        for e in company:
            if e[0] == number:
                testanto = False
                print("Flight: ", e[0])
                test = len(e[1])
                quant = int(input("Quantas reservas vocÊd eseja: "))
                if quant <= test:
                    del e[1][:quant]
                    print("\n")
                else:
                    print("Não há vagas!")
        if testando:
            print("Não existe esse voo!")
        if not testando:
            for e in company:
                if e[0] == number and len(e[1]) == 0:
                    del e
        

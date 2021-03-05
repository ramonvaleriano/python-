# Program: Algoritmo365_Vetor13.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/04/2020 - 11:10
# Updated:

data = dict()
quantity = 2

for e in range(quantity):
    checks = list()
    while True:
        code = int(input("Enter with the code: "))
        if code > 0 :
            value = float(input("Enter with the value: "))
            if value > 0:
                date = int(input("Enter with the date in the format, ddmmaaaa: "))
                if date >= 1000000 and date <= 99999999:
                    day = int(date/1000000)
                    month = int((date%1000000)/10000)
                    year = int(date%10000)
                    print(day, month, year)
                    if(((day>=1)and(day<=31))and((month>=1)and(month<=12))
                       and((year>=1)and(year<9999))):
                        destiny = str(input("Enter with the destiny: "))
                        destiny = destiny.upper()
                        checks.append(value)
                        checks.append(day)
                        checks.append(month)
                        checks.append(year)
                        checks.append(destiny)
                        data[code]=checks
                        break
                    else:
                        print("Invalid Option!")
                else:
                    print("Invalid Option!")
            else:
                print("Invalid Option!")
        else:
            print("Invalid Option!")
print("\n\n")
for k, v in data.items():
    print("Code: %d" %k)
    print("R$%7.2f - Date: %02d/%02d/%4d - Destiny: %12s" %(v[0],v[1],v[2],v[3],v[4]))
    print("\n")

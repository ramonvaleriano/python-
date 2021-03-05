# Program: Algoritmo306_Enq45.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 07/04/2020 - 07:42
# Updated:

cont = 0
value_service = 0.47
account = 0
bigger = 0
account_totat = 0
while True:
    codig = int(input("Enter with codig wht subscriber: "))
    if codig <=0:
        break
    type_ = input("Type is Commercial or Residential: ")
    type_ = type_.upper()
    pulse = int(input("Enter with the quantity of pulse: "))
    service = input("Enter with quantity of service, Yes or Not:")
    service = service.upper()
    if type_ == "RESIDENTIAL":
        tax = 23
        account = tax*pulse
        if pulse >= 90:
            rest = pulse - 90
            result = 0.10*rest
            account = account + result
        if service == "YES":
            account = account + value_service
            
    elif type_ == "COMMERCIAL":
        tax = 30
        account = tax*pulse
        if pulse >= 90:
            rest = pulse - 90
            result = 0.10*rest
            account = account + result
        if service == "YES":
            account = account + value_service
    else:
        print("Invalid Option!")

    if bigger<=account:
        bigger = account
        codig_b = codig
    cont+=1
    account_totat+=account
    print(codig)
    print(account)
media = account_totat / cont 
print() 
print(bigger)
print(codig_b)
print(media)

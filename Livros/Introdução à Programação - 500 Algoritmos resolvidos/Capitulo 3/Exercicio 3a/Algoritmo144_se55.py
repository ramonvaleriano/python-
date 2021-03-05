# Program: Algoritmo144_se55.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 09:18
# Updated:

balance = float(input("Enter with your balance: "))

if(balance>0)and(balance<=500):
    tax = 0
elif(balance>500)and(balance<=1000):
    tax = 30
elif(balance>1000)and(balance<=3000):
    tax = 40
elif(balance>300)and(balance<=1000):
    tax = 30
else:
    print("What fuck is this?!")

conversion = (balance*tax)/100
value = (balance*2)/100

print(balance)
print(conversion)
print(conversion+value)



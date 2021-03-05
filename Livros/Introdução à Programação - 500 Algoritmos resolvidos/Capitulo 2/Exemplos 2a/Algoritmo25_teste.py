# Program: Algoritmo25_teste.py
# Author: Ramon R. Valeraino
# Description:
# Developed: 14/03/2020 - 15:39
# Updated:

date_complete = int(input("Enter with a complete date: "))
day = int(date_complete/1000000)
month = int((date_complete%1000000)/10000)
year = int(date_complete%10000)

print("%02d" %day)
print("%02d" %month)
print("%02d" %year)


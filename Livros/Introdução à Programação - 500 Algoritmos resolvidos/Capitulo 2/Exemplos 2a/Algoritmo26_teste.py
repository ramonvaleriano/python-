# Program: Algoritmo26_teste.py
# Author: Ramon R. Valeraino
# Description:
# Developed: 14/03/2020 - 15:49
# Updated:

date_complete = int(input("Enter with a complete date: "))
day = int(date_complete/1000000)
month = int((date_complete%1000000)/10000)
year = int(date_complete%10000)

month_new = month*1000000 
day_new = day*10000
date_new = int(month_new+day_new+year)
print(date_new)

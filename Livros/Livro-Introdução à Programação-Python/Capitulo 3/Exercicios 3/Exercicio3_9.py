# Program: Exercicio3_9.py
# Author: Ramon R. Valeriano
# Descripiton:
# Developed: 23:07 - 11/03/2020
# Updated:

hour = int(input("Enter with the hour: "))
minute = int(input("Enter with the minutes: "))
seconds = int(input("Enter with the seconds: "))

conversion1 = hour*3600
conversion2 = minute*60

sum_= conversion1+conversion2+seconds

print(sum_)

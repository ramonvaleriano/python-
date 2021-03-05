# Program: Algoritmo264_Enq3.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 11:13
# Updated:
cont = 0
number = int(input("Enter with a number %d°: " %(cont+1)))
sum_=0
while number>=0:
    cont+=1
    number = int(input("Enter with a number %d°: " %(cont+1)))
    sum_+=number
media=sum_/cont
print(media)


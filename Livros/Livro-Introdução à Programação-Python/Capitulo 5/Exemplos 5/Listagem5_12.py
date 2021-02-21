# Program: Listagem5_12.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 07:20
# Updated:

n = 1
sum_ = 0
while n<=5:
    number=int(input("Enter with number to sum: "))
    sum_+= number
    n+=1
print()
print(sum_)
print(n-1)
media=(sum_/(n-1))
print(media)

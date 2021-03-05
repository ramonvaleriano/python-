# Program: Algoritmo81_leia54.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/03/2020 - 19:17
# Updated:

number = int(input("Enter with number: "))

centesimal = int(number/100)
decimal = int((number%100)/10)
unitary = int(number%10)
reverse = (unitary*100)+(decimal*10)+centesimal
print(reverse)
sum_ = number + reverse
print(sum_)
centesimal1 = int(sum_/100)
decimal1 = int((sum_%100)/10)
unitary1 = int(sum_%10)
result = (centesimal1*1)+(decimal1*2)+(unitary1*3)
print(result)
verification = result%10
print(verification)

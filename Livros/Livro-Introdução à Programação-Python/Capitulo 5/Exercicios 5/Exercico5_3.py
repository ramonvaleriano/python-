# Program: Exercico5_3.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 28/03/2020 - 21:11
# Update:

number = 10

while number>=0:
    print(number)
    
    if number == 0:
        print("Fogo!")
    number-=1

print("\n")

for e in range(10, -1, -1):
    print(e)
    if e == 0:
        print("Fogo!")

# Program: Listagem8_4EuMesmo.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/06/2020 - 20:18
# Updated:

def ehpar(number):
    test = number%2==0
    return test
def definicao(number):
    if ehpar(number):
        message = "Esse número é par!"
        return message
    else:
        message = "Esse número é impar!"
        return message
print("{0} é {1}".format(2, definicao(2)))
print("{0} é {1}".format(3, definicao(3)))
print("{0} é {1}".format(10, definicao(10)))

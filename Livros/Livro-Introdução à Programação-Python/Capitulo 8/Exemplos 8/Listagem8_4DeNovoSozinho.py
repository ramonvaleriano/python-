# Program: Listagem8_4DeNovoSozinho.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 10:15
# Updated:

def ehpar(number):
    test = number%2==0
    return test
def testando(number):
    if ehpar(number):
        message = "É Par!"
    else:
        message = "É Ímpa!"
    return message
print("{0} {1}".format(2, testando(2)))
print("{0} {1}".format(3, testando(3)))
print("{0} {1}".format(10, testando(10)))

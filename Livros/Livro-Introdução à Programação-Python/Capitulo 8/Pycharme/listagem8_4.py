# Program: listagem8_4.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 15/09/2020 - 21:05

def ehpar(a):
    return(a%2==0)
def ehimpar(b):
    if ehpar(b):
        return 'É Par!'
    else:
        return 'É ímpar!'

print(ehimpar(4))
print(ehimpar(3))
print(ehimpar(9))
print(ehimpar(6))
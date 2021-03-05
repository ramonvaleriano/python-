# Program: arranjo.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/06/2020 - 16:49
# Updated:

def numerador(number):
    fat = 1
    while number>0:
        fat*=number
        number-=1
    return fat

def test(number1, number2):
    if (number1-number2)>0:
        return True
    else:
        return False
def test2(number3):
    if number3>0:
        return True
    else:
        return False

def denominador(number1, number2, testando, acima):
    if testando(number1, number2):
        result = (number1-number2)
        return(acima(result))
        
def formula(acima, abaixo, number1, number2, testando):
    if abaixo(number1, number2, testando, acima)>0:
        result = (acima(number1))/(abaixo(number1, number2, testando, acima))
        return result
    else:
        return None

def formula2(acima, abaixo, number1, number2, number3, testando, testando2):
    if (abaixo(number1, number2, testando, acima)>0)and(number3>0):
        result = (acima(number1))/(abaixo(number1, number2, testando, acima)*acima(number3))
        return result
    else:
        return None


        

# Program: desafio_034.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 11:56

salary = float(input('Digite o seu salario: '))
if salary>=1250:
    new_salary = salary + ((salary*10)/100)
    print(new_salary)
else:
    new_salary = salary + ((salary * 15) / 100)
    print(new_salary)
# Program: Algoritmo105_se16.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 24/03/2020 - 17:08
# Updated:

symbol = input("Enter with your symbol: ")

if (symbol == "RJ") or (symbol == "rj") or (symbol == "Rj"):
    result = "Carioca"
elif (symbol == "SP") or (symbol == "sp") or (symbol == "Sp"):
    result = "Paulista"
elif (symbol == "MG") or (symbol == "mg") or (symbol == "Mg"):
    result = "Minero"
else:
    result = "Outros estados"
print(result)

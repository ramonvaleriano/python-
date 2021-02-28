# Program: exercicio10_8.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 24/02/2020 - 10:34

from clientes import Cliente
from exercicio10_7 import Conta

valeriano = Cliente("Ramon R. Valeriano", "071 9 9277-4903")
gabriela = Cliente("Milla G. B. D. Valeriano", "12345678901")

joao = Cliente("João Maria", "934275348")
jose = Cliente("Jose Teledo", "64896734957")

conta1 = Conta([valeriano], 148909, 1000)
conta2 = Conta([valeriano, gabriela], 7092019, 5000)
conta3 = Conta([joao], 123456, 456)
conta4 = Conta([jose], 78946, 3216)

print(conta3.clientes)
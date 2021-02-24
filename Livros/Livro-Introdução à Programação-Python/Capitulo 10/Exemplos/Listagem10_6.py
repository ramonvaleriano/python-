# Program: listagem10_6.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 24/02/2020 - 10:05

from clientes import Cliente
from contas2 import Conta

valeriano = Cliente("Ramon R. Valeriano", "071 9 9277-4903")
gabriela = Cliente("Milla G. B. D. Valeriano", "12345678901")

conta1 = Conta([valeriano], 148909, 0)
conta2 = Conta([valeriano, gabriela], 7092019, 0)

print(conta1.saldo)
print(conta2.saldo)
conta1.deposito(1000)
conta2.deposito(50000)
print(conta1.saldo)
print(conta2.saldo)
conta1.extrado


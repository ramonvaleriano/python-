# Program: exercicio10_11.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 27/02/2020 - 22:56

from contas2 import Conta

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self._limite = limite

    def saque(self, valor):
        if self.saldo + self._limite >= valor:
            self.saldo-=valor
            self.operacoes.append(['Saque', valor])
            print(f'Saque realizado no valor de {valor}')
        else:
            print(f'Saque não realizado!')

    def extrado(self):
        print(f'O limite total disponivel para saque é R$ {self.saldo+self._limite}')

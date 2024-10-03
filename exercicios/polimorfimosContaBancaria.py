from abc import ABC, abstractmethod


class Conta(ABC):
    @abstractmethod
    def movimentacao(self, saldo, valor):
        pass


class Saque(Conta):
    def movimentacao(self, saldo, valor):
        return saldo - valor


class Deposito(Conta):
    def movimentacao(self, saldo, valor):
        return saldo + valor

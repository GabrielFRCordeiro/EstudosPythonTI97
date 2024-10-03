from abc import ABC, abstractmethod


class Operacao(ABC):
    @abstractmethod
    def operacao(self, valor1, valor2):
        pass


class Adicao(Operacao):
    def operacao(self, valor1, valor2):
        return valor1 + valor2


class Substracao(Operacao):
    def operacao(self, valor1, valor2):
        return valor1 - valor2


class Multiplicacao(Operacao):
    def operacao(self, valor1, valor2):
        return valor1 * valor2


class Divisao(Operacao):
    def operacao(self, valor1, valor2):
        return valor1 / valor2


def calculadora(*args):
    v1 = args[0]
    v2 = args[1]
    v3 = args[3](v1, v2)

"""
•Criar uma Classe Personagem que contem: nome e arma,
- A arma vai entrar somente através de um setter
•
•Você vai criar uma classe abstrata Arma: modelo, dano e alcance
-A classe Arma vai ter um método abstrato chamado atirar
•
Crie duas Armas sendo filhas de Arma: Arco e flecha , Revolver
"""

from abc import ABC, abstractmethod


class Arma(ABC):
    def __init__(self, modelo, dano, alcance):
        self.__modelo = modelo
        self.__dano = dano
        self.__alcance = alcance

    @abstractmethod
    def atirar(self):
        pass


class ArcoEFlecha(Arma):
    def atirar(self):
        return 1


class Revolver(Arma):
    def atirar(self):
        return 2


class Personagem:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__arma = None

    @property
    def arma(self):
        return self.__arma

    @arma.setter
    def arma(self, arma: Arma):
        self.__arma = arma


if __name__ == '__main__':
    p1 = Personagem('Zé')
    print(p1.arma)

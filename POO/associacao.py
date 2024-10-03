from abc import ABC


class Ferramenta(ABC):
    def __init__(self, nome, marca):
        self.__nome = nome
        self.__marca = marca


class Caneta(Ferramenta):
    pass

aaa = Caneta('oi', 'a')
print(type(aaa).__name__)

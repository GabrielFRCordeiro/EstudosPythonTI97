from abc import ABC, abstractmethod
from datetime import date


class Classe1(ABC):
    def __init__(self, nome: str = 'Carlão') -> None:
        self.__nome = nome
        self.__oculto = None
        self.__cont = 0


    @property
    def nome(self) -> str:
        return self.__nome


    @nome.setter
    def nome(self, novoNome: str) -> None:
        self.__nome = novoNome

    def contar(self) -> int:
        """
        O metodo contar soma mais 1 valor cada uma de suas chamadas e retorna o valor somado
        :return:
        """
        self.__cont += 1
        return self.__cont

    @abstractmethod
    def calcularIdade(self):
        pass


class Classe2(Classe1):
    def __init__(self, nome, salario: float, anoNasc: int) -> None:
        super().__init__(nome)
        self.__salario: float = salario
        self.__anoNasc: int = anoNasc


    @property
    def salario(self) -> float:
        return self.__salario


    @salario.setter
    def salario(self, novoSalario: float) -> None:
        self.__salario = novoSalario


    def calcularIdade(self) -> int:
        anoAtual = date.today().year
        idade = anoAtual - self.__anoNasc
        return idade


if __name__ == '__main__':
    t2 = Classe2('Matias', 1.99)
    print(t2.salario)
    print(t2.nome)
    print(t2.contar())

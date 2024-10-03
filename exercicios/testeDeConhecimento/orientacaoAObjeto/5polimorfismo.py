from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.__idade = idade

    @abstractmethod
    def cumprimentar(self):
        pass

    @property
    def idade(self):
        return self.__idade


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, nota: float):
        super().__init__(nome, idade)
        self.nota = nota

    def estudar(self):
        self.nota += 1

    def cumprimentar(self):
        print(f'Oi, {self.nome}!')


class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, disciplina: str):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def cumprimentar(self):
        print(f'Olá, hoje vamos aprender {self.disciplina}!')


rogerio = Professor('Rogério', 39, 'Sistemas')

rogerio.cumprimentar()

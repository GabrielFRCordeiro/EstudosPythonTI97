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


class Curso:
    def __init__(self, nome: str):
        self.nome = nome
        self.listaAlunos = list()

    def addAluno(self, *args):
        for aluno in args:
            self.listaAlunos.append(aluno)


    def mediaNotas(self):
        soma = 0
        for aluno in self.listaAlunos:
            soma += aluno.nota
        return soma / len(self.listaAlunos)


dani = Aluno('Daniele', 21, 6)
jhow = Aluno('Jonathas', 33, 8)
mateus = Aluno('Mateus', 20, 7)
senac = Curso('TI97')
senac.addAluno(dani, jhow, mateus)
print(senac.mediaNotas())

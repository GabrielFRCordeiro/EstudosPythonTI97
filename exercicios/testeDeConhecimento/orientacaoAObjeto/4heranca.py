from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.__idade = idade

    def cumprimentar(self):
        print(f'Oi, {self.nome}!')

    @property
    def idade(self):
        return self.__idade


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, nota: float):
        super().__init__(nome, idade)
        self.nota = nota

    def estudar(self):
        self.nota += 1


gege = Aluno('Giovani', 17, 6)

print(gege.nota)
gege.estudar()
print(gege.nota)

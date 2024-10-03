class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.__idade = idade

    def cumprimentar(self):
        print(f'Oi, {self.nome}!')

    @property
    def idade(self):
        return self.__idade


ravi = Pessoa('Raviel', 21)

print(ravi.idade)

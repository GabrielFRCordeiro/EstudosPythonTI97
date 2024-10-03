class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f'Oi, {self.nome}!')


ravi = Pessoa('Raviel', 21)

ravi.cumprimentar()

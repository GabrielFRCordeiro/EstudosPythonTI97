class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


ravi = Pessoa('Raviel', 21)

print(f'{ravi.nome} tem {ravi.idade} anos')

class Carro:
    # Atributo de class
    marca = 'GM'

    def __init__(self, cor, modelo, placa):
        self.cor = cor
        self.modelo = modelo
        self.placa = placa


c1 = Carro('Preto', 'SUV', 'AAA-1234')
c2 = Carro('Azul', 'Sedan', 'UNO-0001')

print(c1.marca)
print(c2.marca)


class Aluno:
    def __init__(self, nome: str, notas: list, ra: str) -> None:
        self.nome = nome
        self.notas = notas
        self.ra = ra
        self.media = 0


    def mudarNome(self, novoNome: str) -> str:
        self.nome = novoNome
        return self.nome

    def calcularMedia(self):
        self.media = sum(self.notas) / len(self.notas)
        return self.media


aluno1 = Aluno('Genilson', [6, 6, 6, 6], '2938434223')
aluno2 = Aluno('Geraldo', [7, 7, 7, 7], '2938434224')

print(aluno1.calcularMedia())
print(aluno2.calcularMedia())
print(aluno2.mudarNome('Geronésio'))

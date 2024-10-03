class Informacoes:
    def __init__(self, nome, anoLancamento):
        self.nome = nome
        self.anoLancamento = anoLancamento


class Personagens:
    def __init__(self, protagonista, vilao, coadjuvante):
        self.protagonista = protagonista
        self.vilao = vilao
        self.coadjuvante = coadjuvante


class Filme:
    def __init__(self, nome, anoLancamento, protagonista, vilao, coadjuvante):
        Informacoes.__init__(self, nome, anoLancamento)
        Personagens.__init__(self, protagonista, vilao, coadjuvante)


if __name__ == '__main__':
    filme = Filme('Homem de Ferro', 2008, 'Tony', 'Monge de Ferro', 'Pepper')
    print(filme.protagonista)

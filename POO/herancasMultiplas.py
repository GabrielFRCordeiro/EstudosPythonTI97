class A:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return 'Eu estou na classe A'


class B:
    def __init__(self, telefone):
        self.telefone = telefone

    def falar(self):
        return 'Eu estou na classe B'


class C(A, B):
    def __init__(self, nome, telefone):
        A.__init__(self, nome)
        B.__init__(self, telefone)


if __name__ == '__main__':
    c = C('oi', '2')
    print(c.nome)

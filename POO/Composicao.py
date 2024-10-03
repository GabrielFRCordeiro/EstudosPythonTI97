class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado


class Contato:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.endereco = None
        self.contato = None

    def addEndereco(self, rua, numero, bairro, cidade, estado):
        self.endereco = Endereco(rua, numero, bairro, cidade, estado)

    def addContato(self, telefone, email):
        self.contato = Contato(telefone, email)


c1 = Cliente('João', '472.159.357-85')
c1.addEndereco('Rua Arroz', 33, 'Tucuruvi', 'São Paulo', 'SP')
c1.addContato('4002-8922', 'jaozin11@gmail.com')

print(c1.nome)
print(c1.contato.login)
print(c1.contato.senha)
print(c1.endereco.rua)

import os

usuarios = list()
somaIdades = 0


def addUsuario(nomeUsuario: str, idadeUsuario: int) -> None:
    novoUsuario = {
        'nome': nomeUsuario,
        'idade': idadeUsuario
    }
    usuarios.append(novoUsuario)


for i in range(4):
    os.system('cls') or None
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    somaIdades += idade
    addUsuario(nome, idade)

media = somaIdades / len(usuarios)

os.system('cls') or None

for usuario in usuarios:
    if usuario['idade'] > media:
        print(usuario['nome'])

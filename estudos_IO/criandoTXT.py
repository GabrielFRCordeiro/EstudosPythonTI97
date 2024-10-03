def addNomes(nome: str) -> None:
    arquivo = open('pessoas.txt', 'a', encoding='utf-8')
    arquivo.write(f'{nome.strip().title()}\n')
    arquivo.close()


def listarNomes() -> list:
    arquivo = open('pessoas.txt', 'r', encoding='utf-8')
    lista = list()
    for linha in arquivo.readlines():
        lista.append(linha.replace('\n', ''))
    arquivo.close()
    return lista


print(listarNomes())


def addAluno(nome: str, nota: float):
    with open('alunos.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome.strip().title()}|{nota}\n')


addAluno('Jonas', 4.7)


def lerAlunos():
    pass

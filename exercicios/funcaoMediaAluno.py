def nomeAluno(aluno: str) -> str:
    nome = aluno
    return nome


def notasAluno(n1, n2, n3, n4) -> list:
    listaNotas = [n1, n2, n3, n4]
    return listaNotas


def calcularMedia(notas) -> float:
    media = sum(notas) / len(notas)
    return media


print(f'A média de {nomeAluno('Geronésio')} é {calcularMedia(notasAluno(8, n3=6, n2=7, n4=8))}')

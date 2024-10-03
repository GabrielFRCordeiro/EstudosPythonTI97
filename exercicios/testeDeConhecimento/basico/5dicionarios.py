from typing import List

alunos = [{
    'aluno': 'João',
    'notas': [6, 6, 5, 7]
}, {
    'aluno': 'Gustavo',
    'notas': [7, 7, 6, 6]
}, {
    'aluno': 'Manuela',
    'notas': [8, 7, 8, 7]
}]


def mediaAluno(aluno: str, notas: List) -> None:
    media = sum(notas) / len(notas)
    print(f'A média de {aluno} é {media}')


mediaAluno(alunos[0]['aluno'], alunos[0]['notas'])
mediaAluno(alunos[1]['aluno'], alunos[1]['notas'])
mediaAluno(alunos[2]['aluno'], alunos[2]['notas'])

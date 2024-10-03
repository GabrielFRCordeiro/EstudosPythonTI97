alunos = [{
    'nome': 'Genivaldo',
    'notas': [5, 5, 5, 5]
}, {
    'nome': 'Genésio',
    'notas': [7, 6, 6.5, 8]
}, {
    'nome': 'Genilson',
    'notas': [8, 8, 8, 8]
}, {
    'nome': 'Germano',
    'notas': [2, 3, 2, 10]
}]

media = 0

for aluno in alunos:
    media = sum(aluno['notas']) / len(aluno['notas'])
    print(f'A média de {aluno['nome']} é {media}')

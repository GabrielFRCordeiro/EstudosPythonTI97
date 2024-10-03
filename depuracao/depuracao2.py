def calcular_media(notas):
    import pdb; pdb.set_trace()
    if len(notas) == 0:
        return 0

    total = sum(notas)
    media = total/len(notas)
    return media


notas_aluno1 = [7.5, 8.0, 6.5]
notas_aluno2 = []

media_aluno1 = calcular_media(notas_aluno1)
print(f'Média do aluno 1: {media_aluno1}')

media_aluno2 = calcular_media(notas_aluno2)
print(f'Média do aluno 2: {media_aluno2}')

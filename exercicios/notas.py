notas = [8, 8, 8, 8]
index = 0
soma = 0

while index < len(notas):
    notas[index] = float(input(f'Qual foi a sua {(index + 1)}ª nota? '))
    soma += notas[index]
    index += 1

media = soma / len(notas)
print(f'A sua média é {media}')

if media > 7 and media <= 10:
    print('Parabéns, você passou de ano!')
elif media > 5 and media <= 7:
    print('Só mais uma prova')
elif media >= 0 and media <= 5:
    print('Burrão vc')
else:
    print('Tá mentindo a nota, sacana!')

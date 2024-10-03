nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media <= 10:
    print('Parabéns, passou de ano!')
elif media >= 5 and media < 7:
    print('Tá quase, só mais uma prova')
elif media >= 0 and media < 5:
    print('Burrão vc')
else:
    print('Tá mentindo a nota, safado!')

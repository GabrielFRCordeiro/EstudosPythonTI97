nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome.upper() == 'PEDRO' and idade >= 18:
    print('=======================================')
    print('===== Bem Vindo(a) ao Jhow Videos =====')
    print('=======================================')
    print()
    print(f'Bem vindo de volta, {nome}')
else:
    print('Vaza, muleke!')

try:
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        print(f'{numero} é um número par')
    else:
        print(f'{numero} é um número ímpar')
except ValueError:
    print('O que você digitou não é um número inteiro!')

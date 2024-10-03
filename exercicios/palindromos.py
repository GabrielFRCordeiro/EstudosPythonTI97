palavra = input('Digite uma palavra para verificação: ')

if palavra == palavra[::-1]:
    print('Sua palavra é um palíndromo')
else:
    print('Sua palavra não é um palíndromo')

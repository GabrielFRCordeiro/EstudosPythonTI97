try:
    numero = float(input('Digite um número: '))

    if numero > 0:
        print(f'O número {numero} é positivo')
    elif numero < 0:
        print(f'O número {numero} é negativo')
    else:
        print(f'O número {numero} é igual a zero')
except ValueError:
    print(f'O que você digitou não é um número')

# Modo estranho de fazer

"""
numero1 = input('Digite um valor: ')
numero2 = input('Digite outro valor: ')
numero1Ghost = numero1.replace('.', '')
numero2Ghost = numero2.replace('.', '')

if numero1Ghost.isnumeric() and numero2Ghost.isnumeric():
    numero1 = float(numero1)
    numero2 = float(numero2)
    print(numero1 + numero2)
else:
    print('Você precisa digitar um número, por favor')
"""

# Modo limpo

try:
    numero1 = float(input('Digite um valor: '))
    numero2 = float(input('Digite outro valor: '))
    print(numero1 / numero2)
except ValueError as valor:
    print('Você precisa digitar um número, por favor')
    print(f'Erro: {valor}')
except ZeroDivisionError as zero:
    print('Impossível dividir por zero')
    print(f'Erro: {zero}')
except Exception as erro:
    print(f'Erro: {erro}')

print('Continua o meu código normalmente')

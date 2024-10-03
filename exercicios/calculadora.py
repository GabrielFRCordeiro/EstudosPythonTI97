"""
n1
n2
operação
match
"""

valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))

operacao = input("""
Qual operação gostaria de realizar?
+ (Adição)
- (Subtração)
* (Multiplicação)
/ (Divisão)
R: """)

print()

match operacao:
    case '+':
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
    case '-':
        print(f'{valor1} - {valor2} = {valor1 - valor2}')
    case '*':
        print(f'{valor1} * {valor2} = {valor1 * valor2}')
    case '/':
        print(f'{valor1} / {valor2} = {valor1 / valor2}')

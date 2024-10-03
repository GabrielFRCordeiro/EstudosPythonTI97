valor1 = float(input('Digite o primeiro valor: '))
operacao = input('''Qual operação deseja realizar?
1) Adição
2) Subtração
3) Multiplicação
4) Divisão
R: ''')
valor2 = float(input('Digite o segundo valor: '))

match operacao:
    case '1':
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
    case '2':
        print(f'{valor1} - {valor2} = {valor1 - valor2}')
    case '3':
        print(f'{valor1} * {valor2} = {valor1 * valor2}')
    case '4':
        print(f'{valor1} / {valor2} = {valor1 / valor2}')

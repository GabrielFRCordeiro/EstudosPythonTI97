verificacao: str = 'SIM'

while verificacao[0] == 'S':
    print("""
===============================================
================= CALCULADORA =================
===============================================
    """)

    valor1 = float(input('Digite o primeiro valor: '))
    operacao = input("""Qual operação deseja realizar?
    1) Adição
    2) Subtração
    3) Multiplicação
    4) Divisão
    5) Potência
    6) Raiz
    7) Porcentagem
    R: """)
    valor2 = float(input('Digite o segundo valor: '))

    match operacao:
        case '1':
            print(valor1 + valor2)
        case '2':
            print(valor1 - valor2)
        case '3':
            print(valor1 * valor2)
        case '4':
            print(valor1 / valor2)
        case '5':
            print(valor1 ** valor2)
        case '6':
            print(valor1 ** (1 / valor2))
        case '7':
            print(valor1 * valor2 / 100)
    verificacao = input('Deseja continuar? ').upper()

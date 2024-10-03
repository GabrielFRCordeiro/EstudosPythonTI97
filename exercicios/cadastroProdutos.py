from datetime import date

produto: str = ''
preco: float = 0
data: str = ''
quantidade: int = 0
total: float = 0

print(' SISTEMA DE CADASTRO '.center(60, '='))
print()

while True:
    opcao = input("""
    O que deseja fazer?

    1) Cadastrar
    2) Listar produtos
    3) Valor total
    4) Sair

    R: """)
    print()

    match opcao:
        case '1':
            print(' CADASTRAR '.center(60, '='))
            print()
            produto = input('Produto: ')
            preco = float(input('Preço: '))
            data = str(date.today())
            quantidade = int(input('Quantidade: '))
            total += (preco * quantidade)
            print()
            print('Produto cadastrado com sucesso!')
            print()
        case '2':
            print(' LISTAR PRODUTOS '.center(60, '='))
            print()
            print(f'Produto: {produto} | Preço: {preco} | Data: {data} | Quantidade: {quantidade}')
            print()
        case '3':
            print(' VALOR TOTAL '.center(60, '='))
            print()
            print(f'R${total}')
            print()
        case '4':
            break

print('Sistema encerrado')

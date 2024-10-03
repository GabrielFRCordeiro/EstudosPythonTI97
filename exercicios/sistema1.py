from datetime import date

nome: str = ''
ano_nascimento: str = ''
telefone: str = ''
salario: float = 0
idade: int = 0

print(' Sistema de Cadastro '.center(60, '='))
print()

while True:
    print(' Seja Bem Vindo(a) '.center(60, '='))
    print()
    opcao = input("""
    O que deseja fazer?
        
    1) Cadastrar
    2) Mostrar usuário
    3) Sair
    
    R: """)
    print()

    match opcao:
        case '1':
            print(' Cadastrar '.center(60, '='))
            print()
            nome = input('Nome: ')
            ano_nascimento = input('Ano de nascimento: ')
            telefone = input('Telefone: ')
            salario = float(input('Salário: '))
            print()
            print('Cliente cadastrado com sucesso!')
            print()
        case '2':
            idade = date.today().year - int(ano_nascimento)
            print(' Mostrar Usuário '.center(60, '='))
            print()
            print(f'Nome: {nome} | Idade: {idade} | Telefone: {telefone} | Salário: {salario}')
            print()
            retornar = input("[Retornar (Enter)]")

        case '3':
            break

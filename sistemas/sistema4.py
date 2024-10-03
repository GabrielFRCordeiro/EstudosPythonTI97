from datetime import date

print('Testando validação de cpf'.center(50, '#'))

listaPessoas = list()
# login

while True:
    print("""
    Opções:
    1) Cadastrar
    2) Mostrar Dados
    3) Mostrar Idade
    4) Sair
    """)

    option = input('Opção: ')

    match option:
        case '1':
            print('Tela Cadastro'.center(50, '#'))
            name = input('Nome: ').strip().title()
            cpf = input('CPF: ')
            ano_nasc = int(input('Ano de nascimento: '))
            idade = date.today().year - ano_nasc

            if len(listaPessoas) == 0:
                people = {'nome': name, 'cpf': cpf, 'idade': idade}
                listaPessoas.append(people)
            else:
                setCPF = set()
                for person in listaPessoas:
                    setCPF.add(person['cpf'])

                size = len(setCPF)
                setCPF.add(cpf)

                if len(setCPF) == size:
                    print('O CPF já existe')
                else:
                    people = {'nome': name, 'cpf': cpf, 'idade': idade}
                    listaPessoas.append(people)
        case '2':
            print('Tela Mostrar Dados'.center(50, '#'))
            print(listaPessoas)
        case '3':
            print('Tela Mostrar Idade'.center(50, '#'))
            quem = input('De quem você gostaria de consultar a idade? ').strip().title()
            for person in listaPessoas:
                if quem == person['nome']:
                    print(f'{person['nome']} tem {person['idade']} anos')
        case '4':
            break

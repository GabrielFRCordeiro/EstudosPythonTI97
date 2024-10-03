def validarTelefone(telefone: str) -> None:
    telefoneValidacao = telefone.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    if telefoneValidacao.isnumeric() and (len(telefoneValidacao) == 8 or len(telefoneValidacao) == 10):
        print('Seu número é residencial')
    elif telefoneValidacao.isnumeric() and (len(telefoneValidacao) == 9 or len(telefoneValidacao) == 11):
        print('Seu número é de celular')
    else:
        print('Seu número é inválido')


telefone = input('Digite seu telefone: ').strip()

validarTelefone(telefone)

def validaTelefone(telefone: str):
    validacao = telefone.replace('-', '')
    if len(validacao) == 8 and validacao.isnumeric():
        return 'fixo'
    elif len(validacao) == 9 and validacao.isnumeric():
        return 'celular'
    else:
        return False

numero = input('Digite um número de telefone: ')

if validaTelefone(numero) == 'fixo':
    print('Este é um telefone fixo')
elif validaTelefone(numero) == 'celular':
    print('Este é um número de celular')
else:
    print('Este não é um número de telefone')

# -*- encode: utf-8 -*-

estudante = {
    'nome': 'Carlos',
    'idade': 44,
    'telefone': '11 4545-4545'
}

print(estudante['nome'])  # pega valor de uma chave
print(estudante.keys())  # pega chaves
print(estudante.values())  # pega valores
print(estudante.items())  # pega chaves e valores em tuplas

escola = dict()  # cria dicionario vazio

# inserindo valores
escola['endereço'] = 'Rua Pedro José'
escola['nome'] = 'EEPSG prof. yoda'
escola['telefone'] = '119999-9999'
print(escola.items())

print('-' * 50)
estudante['notas'] = [4.5, 7, 8, 9]
print(estudante['notas'][2])
print(len(estudante))
print(sum(estudante['notas']) / len(estudante['notas']))  # sum é soma. só funfa se for com numero

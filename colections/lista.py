# Criando lista

# Índice      0           1           2          3
# nomes = ['Genivaldo', 'Genésio', 'Genilson', 'Neuzeti']
#
# # Visualizando os dados
# print(nomes)  # Lista inteira
# print(nomes[0])  # Pega elemento separado
# print(nomes[0:2])  # Pega mais de um elemento
#
# # Regras
# # - Mutabilidade: capacidade de modificar
# nomes[3] = 'Gesonel'  # Precisa estar no range (nesse caso, de 0 a 3)
# print(nomes)
# # nomes[1:3] = 'Gesonel' (Não usar)
# nomes.append('Genésio')
# print('Append:', nomes)
# # - Dinâmico
# # nomes.append(42) (Não deve ser feito)
# nomes.remove('Genilson')
# print('Remove:', nomes)
# print('Count:', nomes.count('Genésio'))
# print('Index:', nomes.index('Genésio', 2, 4))
# nomes2 = nomes
# nomes2[3] = 'Genilson'
# print('Nomes2:', nomes)
# print('Nomes2:', nomes2)
# nomes3 = nomes.copy()
# nomes3[3] = 'Geraldo'
# print('Copy:', nomes)
# print('Copy:', nomes3)
# nomes.insert(1,'Genéses')
# print('Insert:', nomes)
# # nomes.clear() (Apaga td a lista)
# nomes.sort()
# print('Sort:', nomes)  # Põe em ordem alfabética
# nome = nomes.pop(4)
# print('Pop:', nome)
# print('Pop:', nomes)
#
# # Percorrer a lista
bancoDeDados = ['Genilson', 'Genivaldo', 'Genéses', 'Genésio']
# # buscar = input('Buscar: ').strip().title()
# # print(len(bancoDeDados))

index = 0

while index < len(bancoDeDados):
    print(f'Nome: {bancoDeDados[index]}')
    index += 1

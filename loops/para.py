# O para funciona retirando valores de um iterador

numeros = [0, 1, 2, 3, 4, 5]

# for n in numeros:
#     print(n)
#
# for i in range(5):
#     print('sla')

nomes = ['Carlos', 'Pedro', 'Maria', 'Silva', 'Pedro', 'Pedro']

for numero, nome in enumerate(nomes):
    print(f'Nome: {nome} está na posição {numero}')

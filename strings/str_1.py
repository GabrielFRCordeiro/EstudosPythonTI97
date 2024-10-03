# String são caracteres

# indice   0123456
palavra = 'palavra'

print(type(palavra))

# pegando os elementos do iterador
print(palavra[0])
print(palavra[-7])

# slice
print(palavra[1:3])
"""
1 = valor inicial, includente (considera o 1)
3 = valor final, excludente (n considera o 3)
"""
print(palavra[:3])
print(palavra[2:])
print(palavra[:])
print(palavra[:-1])
print(palavra[::])
print(palavra[::2])
print(palavra[::-1])

# metodos
palavra.upper()  # 'PALAVRA'
palavra.lower()  # 'palavra'
print(palavra.center(11, '#'))  # coloca coisas envolta
print('   sei la  '.strip())  # tira espaços do começo e do fim
print(palavra.title())  # 'Palavra' primeira letra vira maiuscula
print(palavra.replace('a', 'o'))  # 'polovro' troca caracteres
print(palavra.isnumeric())  # ve se é um numero
print(palavra.index('a', 2, 6))
print(len(palavra))
print(palavra.count('a'))

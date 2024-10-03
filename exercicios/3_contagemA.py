texto = input('Digite um texto: ')

print(texto.count('a'))

if texto.count('a') > 3:
    print(texto.replace('a', '#'))
else:
    print(texto)

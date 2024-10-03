mensagem = input('Digite um texto ou um número: ')

if mensagem.isalpha():
    print(mensagem)
elif mensagem.isnumeric():
    print(int(mensagem) + 10)
else:
    print('O que você digitou não é só um texto ou só um número')

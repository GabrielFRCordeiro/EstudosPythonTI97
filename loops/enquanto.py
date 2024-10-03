cont = 1

while cont < 10:
    print(f'Estou no loop: {cont}')
    cont += 1

while True:
    resposta = input('Deseja continuar no loop? Sim ou não? ').strip()[0].upper()
    if resposta == 'N':
        break

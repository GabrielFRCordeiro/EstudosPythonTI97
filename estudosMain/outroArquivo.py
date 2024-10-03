from estudosMain.classe import Personagem

toni = Personagem('Toni Bala', 8, 4, 6)

while True:
    print('Digite o valor do movimento: ')
    key = input('Tecla: ')
    toni.movimentar(key)

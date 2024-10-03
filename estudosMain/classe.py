import time


class Personagem:

    def __init__(self, nome, altura, largura, velocidade):
        self.nome = nome
        self.altura = altura
        self.largura = largura
        self.velocidade = velocidade
        self.posicaoX = 0
        self.posicaoY = 0


    def movimentar(self, comando: str):
        match comando:
            case 'd':
                self.posicaoX += self.velocidade
                print(f'{self.nome} está no pixel {self.posicaoX}')
            case 'a':
                self.posicaoX -= self.velocidade
                print(f'{self.nome} está no pixel {self.posicaoX}')
            case 's':
                self.altura /= 2
                print(f'{self.nome} está abaixado')
                time.sleep(3)
                self.altura *= 2
                print(f'{self.nome} está de pé')
            case 'w':
                self.posicaoY += self.velocidade
                print(f'{self.nome} está na altura {self.posicaoY}')
                time.sleep(5)
                self.posicaoY -= self.velocidade
                print(f'{self.nome} está na altura {self.posicaoY}')


if __name__ == '__main__':
    jojo = Personagem('Jojo', 7, 5, 2,)

    while True:
        print('Digite o valor do movimento: ')
        key = input('Tecla: ')
        jojo.movimentar(key)

class Personagem:

    def __init__(self, img: str, nome: str, moveX: int, moveY: int, deslocamento: int = 5) -> None:
        self.__img = img
        self.__nome = nome
        self.__moveX = moveX
        self.__moveY = moveY
        self.__deslocamento = deslocamento

    # Getter
    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, newImg):
        self.__img = newImg

    @property
    def nome(self):
        return self.__nome

    @img.setter
    def nome(self, newNome):
        self.__nome = newNome

    @property
    def moveX(self):
        return self.__moveX

    @moveX.setter
    def moveX(self, newMoveX):
        self.__moveX = newMoveX

    @property
    def moveY(self):
        return self.__moveY

    @moveY.setter
    def moveY(self, newMoveY):
        self.__moveY = newMoveY

    @property
    def deslocamento(self):
        return self.__deslocamento

    @deslocamento.setter
    def deslocamento(self, newDeslocamento):
        self.__deslocamento = newDeslocamento


if __name__ == '__main__':
    p1 = Personagem('carlos.png', 'Carlos', 0, 0)

    print(p1.moveY)

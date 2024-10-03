class Objeto:
    def __init__(self, img: str, posX: int, posY: int) -> None:
        self.__img = img
        self.__posX = posX
        self.__posY = posY

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, newImg):
        self.__img = newImg

    @property
    def posX(self):
        return self.__posX

    @posX.setter
    def posX(self, newPosX):
        self.__posX = newPosX

    @property
    def posY(self):
        return self.__posY

    @posY.setter
    def posY(self, newPosY):
        self.__posY = newPosY

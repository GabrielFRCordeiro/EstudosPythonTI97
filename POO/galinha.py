from datetime import date


class Galinha:
    ovosGranja = 0

    def __init__(self, tipo: str = None, ovos: int = 0) -> None:
        self.tipo = tipo
        self.ovos = ovos
        self.status = True
        self.dataNasc = date.today()
        self.addOvos()

    @classmethod
    def addOvosGranja(cls):
        cls.ovosGranja += 1

    def addOvos(self):
        self.ovos += 1
        Galinha.addOvosGranja()

    def corte(self):
        self.status = False

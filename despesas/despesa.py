from datetime import date


class Despesa:
    totalDespesas = 0

    def __init__(self, descricao: str, valor: float, data: date = date.today()) -> None:
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.status = False

    @classmethod
    def somarDespesas(cls, valor: float) -> None:
        """
        Esse método soma as despesas
        :param valor:
        :return:
        """
        cls.totalDespesas += valor

    def realizarPagamento(self) -> None:
        self.status = True
        self.data = date.today()
        Despesa.somarDespesas(self.valor)

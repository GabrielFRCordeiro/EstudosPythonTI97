from datetime import date

class User:

    def __init__(self, nome: str, senha: str, dataNasc: date = None) -> None:
        self.nome = nome
        self.senha = senha
        self.dataNasc = dataNasc

    # metodo
    def calculaIdade(self) -> int:
         dataAtual = date.today()
         idade = dataAtual.year - self.dataNasc.year

         if(dataAtual.month, dataAtual.day) < (self.dataNasc.month,self.dataNasc.day):
             idade -= 1

         return idade

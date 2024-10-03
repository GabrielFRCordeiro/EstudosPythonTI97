# import datetime as dt
from datetime import (date, datetime)
# from datetime import *

# Data de hoje
hoje = datetime.today()
hoje_novo = date.today()
data = date(day=23, month=4, year=2023)
dataCompleta = datetime(year=2024, month=5, day=2, hour=11, minute=34, second=55, microsecond=543213)

print(f'Hoje {hoje_novo}')
print(f'Data {data}')
print(dataCompleta)
print(data.strftime('%d %m %Y'))
print(hoje.strftime('%d/%m/%y'))

print('---------------------------------')


def pegarDataAniversario(dia: int, mes: int, ano: int) -> date:
    dataAniversario = date(year=ano, month=mes, day=dia)
    return dataAniversario


dataNascimento = input('Data de nascimento: ')
dia, mes, ano = dataNascimento.split('/')
aniversario = pegarDataAniversario(int(dia), int(mes), int(ano))
print(aniversario)

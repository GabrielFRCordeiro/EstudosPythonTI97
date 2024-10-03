import os
from datetime import date


def jogarNoSistema(jogoRetirado):
    sistema = open('sistema.txt', 'a', encoding='utf-8')
    sistema.write(f'{jogoRetirado}\n')
    sistema.close()


def cadastrarJogo(dataCadastrada, nomeCadastrado, cpfCadastrado, jogoCadastrado):
    retirada = {
        "data": dataCadastrada,
        "nome": nomeCadastrado,
        "cpf": cpfCadastrado,
        "jogo": jogoCadastrado
    }
    return retirada


def validarCPF(cpfValidacao: str):
    if cpfValidacao.count('-') > 0 or cpfValidacao.count('.') > 0:
        cpfValidado = cpfValidacao.replace('-', '').replace('.', '')
        if cpfValidado.isnumeric() and len(cpfValidado) == 11:
            return False
        else:
            return True
    elif cpfValidacao.isnumeric() and len(cpfValidacao) == 11:
        return False
    else:
        return True


def posicionarNaLista(jogoAdd):
    if jogoAdd == '1' or jogoAdd == 'Uno':
        posicao = 0
        return posicao
    elif jogoAdd == '2' or jogoAdd == 'Master':
        posicao = 1
        return posicao
    elif jogoAdd == '3' or jogoAdd == 'Monopoly':
        posicao = 2
        return posicao


def validarJogo(jogoValidacao):
    if jogoValidacao == '1' or jogoValidacao == 'Uno':
        return False
    elif jogoValidacao == '2' or jogoValidacao == 'Master':
        return False
    elif jogoValidacao == '3' or jogoValidacao == 'Monopoly':
        return False
    else:
        return True


listaJogos = [{
    'nomeJogo': 'Uno',
    'resumo': 'O objetivo é ficar com só uma carta'
}, {
    'nomeJogo': 'Master',
    'resumo': 'O objetivo é acertar o máximo de perguntas'
}, {
    'nomeJogo': 'Monopoly',
    'resumo': 'O objetivo é ficar rico'
}]

print("Seja bem-vindo ao Games Senac!".center(50, '='))

data = date.today()
print()

nome = input("Informe seu nome: ").strip().title()
print()

cpf = input("Informe seu cpf: ").strip()

while validarCPF(cpf):
    print()
    cpf = input('CPF inválido, digite outro CPF: ')
print()

print("Qual jogo foi retirado?")

jogoEscolhido = input("""
1) Uno
2) Master
3) Monopoly

Resposta: """).strip().title()

while validarJogo(jogoEscolhido):
    print()
    jogoEscolhido = input('Jogo não encontrado. Por favor, digite novamente: ')
print()

jogarNoSistema(cadastrarJogo(data, nome, cpf, listaJogos[posicionarNaLista(jogoEscolhido)]['nomeJogo']))

os.system('cls') or None

print()
tutorial = input('Você quer um tutorial do jogo? ').strip().upper()
print()

if tutorial[0] == 'S':
    print(listaJogos[posicionarNaLista(jogoEscolhido)]['resumo'])
    print()

print("Divirta-se!")

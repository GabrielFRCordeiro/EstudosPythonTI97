import os
import time
from abc import ABC, abstractmethod

class Filme(ABC):
    def __init__(self, nome: str, ano: int, metragem: int) -> None:
        self.nome = nome
        self.ano = ano
        self.metragem = metragem


class Comedia(Filme):
    pass


class Terror(Filme):
    pass


class Acao(Filme):
    pass


print('\033[20;1;33m Sistema Filmes \033[0;0m')

bancoDados = [{
    'login': 'Toninho',
    'senha': '1111'
}, {
    'login': 'Joelma',
    'senha': '2222'
}]

listaFilmes = list()

while True:
    os.system('cls') or None
    print(' LOGIN '.center(50, '='))
    login = input('\033[20;1m Nome: \033[0;0m').strip().title()
    senha = input('\033[20;1m Senha: \033[0;0m')
    if len(senha) == 4:
        for usuario in bancoDados:
            if usuario['login']==login and usuario['senha']==senha:
                os.system('cls') or None
                print(' MENU '.center(50, '='))
                print('''1) Cadastrar Filmes
2) Checar filmes de comédia
3) Checar filmes de terror
4) Checar filmes de ação
5) Sair''')

                opcao = input('\033[20;1m Opção: \033[0;0m')
                match opcao:
                    case '1':
                        os.system('cls') or None
                        print(' CADASTRAR FILME '.center(50, '='))
                        genero = input('''Qual o gênero do filme a ser cadastrado?
1) Comédia
2) Terror
3) Ação''')
                        opcao = input('\033[20;1m Opção: \033[0;0m')
                        nomeFilme = input('Digite o nome do filme: ').strip().title()
                        anoLancamento = int(input('Digite o ano de lançamento: '))
                        duracao = int(input('Digite a duração do filme: '))
                        match opcao:
                            case '1':
                                filme = Comedia(nomeFilme, anoLancamento, duracao)
                            case '2':
                                filme = Terror(nomeFilme, anoLancamento, duracao)
                            case '3':
                                filme = Acao(nomeFilme, anoLancamento, duracao)
                        listaFilmes.append(filme)
                        print('Adicionado com sucesso!')
                        time.sleep(5)
                    case '2':
                        os.system('cls') or None
                        print(' CHECAR FILMES COMÉDIA '.center(50, '='))
                        for filme in listaFilmes:
                            if type(filme).__name__ == Comedia:
                                print(f'{filme.nome} lançou em {filme.ano} e tem {filme.metragem} minutos')
                                time.sleep(5)
                    case '3':
                        os.system('cls') or None
                        print(' CHECAR FILMES TERROR '.center(50, '='))
                        for filme in listaFilmes:
                            if type(filme).__name__ == Terror:
                                print(f'{filme.nome} lançou em {filme.ano} e tem {filme.metragem} minutos')
                    case '4':
                        os.system('cls') or None
                        print(' CHECAR FILMES AÇÃO '.center(50, '='))
                        for filme in listaFilmes:
                            if type(filme).__name__ == Acao:
                                print(f'{filme.nome} lançou em {filme.ano} e tem {filme.metragem} minutos')
                    case '5':
                        print('Saindo do sistema...')
                        time.sleep(5)
                        break
    else:
        print('A senha deve ter 4 caracteres')


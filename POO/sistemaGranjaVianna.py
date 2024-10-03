import os
from datetime import date
from POO.users import User
from POO.galinha import Galinha
import time

print('\033[20;1;33m Sistema Granja Vianna \033[0;0m')

us1 = User('Toninho', '1111')
us2 = User('Joelma', '2222', date(1997, 4, 13))

bancoDados = {
    'usuarios': [us1, us2],
    'galinhas': []
}

while True:
    os.system('cls') or None
    print(' LOGIN '.center(50, '='))
    nome = input('\033[20;1m Nome: \033[0;0m').strip().title()
    senha = input('\033[20;1m Senha: \033[0;0m')
    if len(senha) == 4:
        for usuario in bancoDados['usuarios']:
            if usuario.nome==nome and usuario.senha==senha:
                os.system('cls') or None
                print(' MENU '.center(50, '='))
                print('''1) Cadastrar Galinha
2) Visualizar quantidade de ovos de cada galinha
3) Visualizar quantidade de ovos da Granja
4) Visualizar usuários
5) Sair''')

                opcao = input('\033[20;1m Opção: \033[0;0m')
                match opcao:
                    case '1':
                        os.system('cls') or None
                        print(' CADASTRAR GALINHA '.center(50, '='))
                        nomeGalinha = input('Digite o nome da galinha: ').strip().title()
                        gg = Galinha(nomeGalinha)
                        bancoDados['galinhas'].append(gg)
                        print('Adicionado com sucesso!')
                        time.sleep(5)
                    case '2':
                        os.system('cls') or None
                        print(' CHECAR OVOS GALINHA '.center(50, '='))
                        nomeChecagem = input('Nome da galinha a ser checada: ').strip().title()
                        for galinha in bancoDados['galinhas']:
                            if nomeChecagem == galinha.tipo:
                                print(f'A {galinha.tipo} tem {galinha.ovos} ovos')
                                time.sleep(5)
                    case '3':
                        os.system('cls') or None
                        print(' CHECAR OVOS GRANJA '.center(50, '='))
                        print(f'A granja tem {Galinha().ovosGranja}')
                        time.sleep(5)
                    case '5':
                        print('Saindo do sistema...')
                        time.sleep(5)
                        break
    else:
        print('A senha deve ter 4 caracteres')

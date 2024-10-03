import math
import os
from datetime import date as dt
import time
print("Sistema de Cadastro".center(60,"-"))
tentativa = False
for cont in range(3):
    os.system("cls") or None
    if tentativa:
        break
    print("Tela Login".center(60,"-"))
    login=input("Login: ").strip().upper()
    password=input("Senha: ").strip()



    if login in ["CARLOS","TONY","GOKU"] and password=="1234":
        tentativa=True
        os.system("cls") or None
        print("Bem vindo ao meu sistema !".center(60, "-"))
        receitas=list()
        despesas=list()
        while True:
            os.system("cls") or None
            print("""
            Options:
            1-) Cadastrar Receitas
            2-) Cadastrar Despesas
            3-) Fluxo de caixa
            4-) Sair
            """)
            option=input("Opção: ")

            match option:
                case "1":
                    os.system("cls") or None
                    print("Cadastrar Receita: ".center(60,"-"))
                    descricao=input("Descrição: ").strip().upper()
                    valor=float(input("Valor R$ "))
                    data=input("Data YYYY-MM-DD: ")
                    status=bool(input("Situação: True ou False"))
                    receita=[descricao,valor,data,status]
                    receitas.append(receita)
                    print("Cadastrado com sucesso !")


                case "2":
                    os.system("cls") or None
                    print("Cadastrar Despesa: ".center(60,"-"))
                    descricao=input("Descrição: ").strip().upper()
                    valor=float(input("Valor R$ "))
                    data=input("Data YYYY-MM-DD: ")
                    status=bool(input("Situação: True ou False"))
                    despesa=[descricao,valor,data,status]
                    despesas.append(despesa)
                    print("Cadastrado com sucesso !")

                case "3":
                    # você deve mostrar quantas receitas e despesas estão cadastradas
                    # você deve mostrar os valores
                    # Você deve fazer a média de despesas
                    os.system("cls") or None

                    print("Fluxo de caixa: ".center(60, "-"))
                    totalReceita=0
                    totalDespesa=0
                    for receita in receitas:
                        totalReceita+=receita[1]

                    for despesa in despesas:
                        totalDespesa+=despesa[1]

                    print("Relatorio".center(60,"-"))
                    print(f"Total de Receitas R${totalReceita}")
                    print(f"Total de Despesas R${totalDespesa}")
                    print(" "*18,"----------")
                    print(" "*18,f"R${totalReceita-totalDespesa}")
                    time.sleep(10)
                case "4":
                    break

    else:
        os.system("cls") or None
        print(f"Nome ou senha não esta no sistema !")
        print(f"{cont + 1}ª tentativa de entrar no sistema !")
        print("Cuidado 3 tentativas vai invalidar sua conta! ")


print("Estou fora do sistema")
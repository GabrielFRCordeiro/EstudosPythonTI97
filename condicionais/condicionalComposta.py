import datetime as dt

# Converter valores

ano_nascimento = int(input('Digite o ano em que nasceu: '))

idade = dt.datetime.now().year - ano_nascimento

if (idade > 0 and idade >= 16 and idade < 18) or (idade >= 70 and idade < 130):
    print('Você pode votar, mas não é obrigado')
elif idade >= 18 and idade < 70:
    print('Você é obrigado a votar')
else:
    print('Você não pode votar')

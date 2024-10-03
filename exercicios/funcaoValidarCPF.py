def retiraSinais(cpf: str):
    if cpf.isnumeric():
        novoCPF = cpf
        return novoCPF
    else:
        novoCPF = cpf.replace('-', '').replace('.', '')
        return novoCPF


def verificaCPF(cpf: str):
    if len(cpf) == 11:
        return 'Este cpf é válido'
    else:
        return 'Este não é um cpf válido'


print(verificaCPF(retiraSinais('12345678901')))

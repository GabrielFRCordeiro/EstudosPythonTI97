livros = [
    {
        'autor': 'Douglas Addams',
        'livro': 'O Guia do Mochileiro das Galáxias',
        'ano': 1979
    },
    {
        'autor': 'Alice Oseman',
        'livro': 'Sem Amor',
        'ano': 2021
    },
    {
        'autor': 'Renata Ventura',
        'livro': 'A Arma Escarlate',
        'ano': 2011
    }
]

for livro in livros:
    print(f'{livro['livro']} foi escrito por {livro['autor']} e lançou em {livro['ano']}')

from objetos.logger import logger
from objetos.material import Material, lista_livros

class Livro(Material):
    def __init__(self, titulo, autores, ano_pub, numero_paginas, editora, genero): 
        super().__init__(titulo, autores, ano_pub)
        self.numero_paginas = numero_paginas
        self.editora = editora
        self.genero = genero

def adicionar_livro():
    titulo = input('\n Digite o título do livro: ')
    autores = []
    ano_pub = input('\n Digite o ano de publicação do livro: ')
    numero_paginas = input('\n Digite o número de páginas que ele possui: ')
    editora = input('\n Insira qual a editora: ')
    genero = input('\n Insira qual é o gênero do livro: ')

    while True:
        autor = input('\n Insira o nome do autor: ')
        autores.append(autor)
        co_autor = input('\n Digite S para adicionar mais um autor, ou pressione enter para seguir: ')
        if co_autor.upper() != 'S':
            break

    livro = Livro(titulo, autores, ano_pub, numero_paginas, editora, genero)
    lista_livros.append(livro)
    logger.novo_material(titulo)

def buscar_livro():
    busca = input('\n Digite o título do livro que deseja localizar: ')
    livros = []
    for livro in lista_livros:
            if busca in getattr(livro, 'titulo'):
                livros.append(livro)

    print(f'\n Resultados encontrados: ')
    for livro in livros:
            print(livro)

    input('\n Enter para seguir')
    
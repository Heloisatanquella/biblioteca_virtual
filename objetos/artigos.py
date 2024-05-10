from objetos.logger import logger
from objetos.material import Material, lista_artigos


class Artigo(Material):
    def __init__(self, titulo, autores, ano_pub, doi, palavras_chave): 
        super().__init__(titulo, autores, ano_pub)
        self.doi = doi
        self.palavras_chave = palavras_chave

def adicionar_artigo():
    titulo = input('\n Digite o título do artigo: ')
    autores = []
    ano_pub = input('\n Digite o ano de publicação do artigo: ')
    doi = input('\n Insira o DOI (Digital Object Identifier) do artigo: ')
    palavras_chave = []

    while True:
        autor = input('\n Insira o nome do autor: ')
        autores.append(autor)
        co_autor = input('\n Digite S para adicionar mais um autor, ou pressione enter para seguir: ')
        if co_autor.upper() != 'S':
            break

    while True:
        palavra_chave = input('\n Insira uma palavra-chave referente ao artigo: ')
        palavras_chave.append(palavra_chave)
        palavra_adicional = input('\n Digite S para adicional mais alguma palavra, ou pressione enter para seguir: ')
        if palavra_adicional.upper() != 'S':
            break

    artigo = Artigo(titulo, autores, ano_pub, doi, palavras_chave)
    lista_artigos.append(artigo)
    logger.novo_material(titulo)

def buscar_artigo():
    busca = input('\n Digite o título, autor ou alguma palavra-chave do artigo que deseja localizar: ')
    artigos = []
    for artigo in lista_artigos:
        if busca in getattr(artigo, 'titulo'):
            artigos.append(artigo)
        elif busca in getattr(artigo, 'palavras_chave'):
            artigos.append(artigo)

    print(f'\n Resultados encontrados: ')
    for artigo in artigos:
            print(artigo)

    input('\n Enter para seguir')

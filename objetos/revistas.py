from objetos.logger import logger
from objetos.utils import novo_codigo
from objetos.material import Material, lista_revistas


class Revista(Material):
    def __init__(self, titulo, editora, ano_pub): 
        self.disponivel = True
        self.id = novo_codigo()
        self.titulo = titulo
        self.editora = editora
        self. ano_pub = ano_pub

def adicionar_revista():
    titulo = input('\n Digite o título da revista: ')
    editora = input('\n Insira qual a editora da revista: ')
    ano_pub = input('\n Insira o mês e o ano de publicação da revista (ex: 12/2024): ')

    revista = Revista(titulo, editora, ano_pub)
    lista_revistas.append(revista)
    logger.novo_material(titulo)

def buscar_revista():
    busca = input('\n Digite o título, a editora da revista que deseja localizar: ')
    revistas = []
    for revista in lista_revistas:
        if busca in getattr(revista, 'titulo'):
            revistas.append(revista)
        elif busca in getattr(revista, 'editora'):
            revistas.append(revista)

    print(f'\n Resultados encontrados: ')
    for revista in revistas:
            print(revista)

    input('\n Enter para seguir')
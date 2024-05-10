from objetos.utils import novo_codigo, buscar

lista_livros = []
lista_artigos = []
lista_revistas = []

class Material:
    def __init__(self, titulo, autores, ano_pub): 
        self.disponivel = True
        self.id = novo_codigo()
        self.titulo = titulo
        self.autores = autores
        self. ano_pub = ano_pub

    def __str__(self) -> str:
        return f'\n ID: {self.id} - {self.titulo} - {self.ano_pub}'


    def alterar_disponibilidade(self):
        if self.disponivel == True:
            self.disponivel = False
        else:
            self.disponivel = True

def buscar_material_por_id() -> Material:
    print('\n Insira o ID do material: ')
    lista_materiais = [*lista_revistas, *lista_artigos, *lista_livros]
    while True:
        id = input()
        material = buscar(int(id), lista_materiais, 'id')
        if material:
            print(material)
            return material
        
        print('\n Material não encontrado. Tente novamente!')


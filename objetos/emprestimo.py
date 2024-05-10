import datetime
from objetos.utils import novo_codigo
from objetos.material import Material, buscar_material_por_id
from objetos.utils import novo_codigo
from objetos.usuario import buscar_usuario
from objetos.logger import logger

class Emprestimo:
    def __init__(self, material, data_emprestimo, data_prazo):
        self.id = novo_codigo()
        self.material: Material = material
        self.data_emprestimo = data_emprestimo
        self.data_prazo = data_prazo
        self.data_devolucao = None

    def __str__(self) -> str:
        return f'\n ID: {self.id} \n Data de empréstimo: {self.data_emprestimo} \n Prazo: {self.data_prazo}'

    def devolver_livro(self):
        self.data_devolucao = datetime.date.today()
        self.material.alterar_disponibilidade()

def alugar_material(usuario, material):
    data_emprestimo = datetime.date.today()
    data_prazo = data_emprestimo + datetime.timedelta(days=7)
    emprestimo = Emprestimo(material, data_emprestimo, data_prazo)
    usuario.historico_emprestimos.append(emprestimo)

def emprestimo():
    material = buscar_material_por_id()
    usuario = buscar_usuario()    
    alugar_material(usuario, material)
    material.alterar_disponibilidade()
    logger.novo_emprestimo(material.titulo)

def devolucao():
    usuario = buscar_usuario()    
    emprestimo = usuario.busca_emprestimo()
    emprestimo.devolver_livro()

    logger.devolucao(emprestimo.material.titulo)
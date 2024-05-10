from objetos.logger import logger
from objetos.utils import buscar

lista_usuarios = []

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.historico_emprestimos = []
    
    def __str__(self) -> str:
        return f'\n Nome: {self.nome} \n E-mail: {self.email}'
    
    def emprestimos_ativos(self):
        ativos = []
        for emprestimo in self.historico_emprestimos:
            if emprestimo.data_devolucao == None:
                ativos.append(emprestimo)

        return ativos
    
    def busca_emprestimo(self):
        emprestimos_ativos = self.emprestimos_ativos()
        for emprestimo in emprestimos_ativos:
            print(emprestimo)

        while True:
            id_emprestimo = input('\n Digite o ID do empréstimo: ')
            emprestimo = buscar(int(id_emprestimo), emprestimos_ativos, 'id')
            if emprestimo:
                return emprestimo
            
            print('\n Não encontrado, tente novamente')


def adicionar_usuario():
    nome = input('\n Insira ao nome do usuário a ser cadastrado: ')
    email = input('\n Insira algum e-mail para contato: ')
    
    usuario = Usuario(nome, email)
    lista_usuarios.append(usuario)
    logger.novo_usuario(nome)

def buscar_usuario() -> Usuario:
    print('\n Insira o e-mail do usuário que você deseja buscar: ')
    while True:
        email = input()
        usuario = buscar(email, lista_usuarios, 'email')
        if usuario:
            print(usuario)
            return usuario
        
        print('\n Usuário não encontrado. Tente novamente!')

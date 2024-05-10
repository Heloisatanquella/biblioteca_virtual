class Logger:
    def __init__(self):
        pass

    def novo_material(self, titulo):
        print(f'\n [ADD] Novo material adicionado com sucesso: {titulo}!')

    def novo_usuario(self, nome):
        print(f'\n [ADD] Novo usuário adicionado com sucesso: {nome}!')

    def novo_emprestimo(self, titulo):
        print(f'\n [Empréstimo] Material emprestado com sucesso: {titulo}!')
    
    def devolucao(self, titulo):
        print(f'\n [Empréstimo] Material devolvido com sucesso: {titulo}!')

logger = Logger()

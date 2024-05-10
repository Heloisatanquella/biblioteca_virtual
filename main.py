from menu.menu import menu, submenu
from objetos.livros import adicionar_livro, buscar_livro
from objetos.artigos import adicionar_artigo, buscar_artigo
from objetos.revistas import adicionar_revista, buscar_revista
from objetos.usuario import adicionar_usuario, buscar_usuario
from objetos.emprestimo import emprestimo, devolucao

# FIXME: fazer o salvamento em arquivos 

def main():
    while True:
        opcao = menu()
        if opcao == 1:
            opcao_submenu = submenu()
            if opcao_submenu == 1:
                adicionar_livro()
            elif opcao_submenu == 2:
                adicionar_artigo()
            elif opcao_submenu == 3:
                adicionar_revista()
            elif opcao_submenu == 4:
                break
        if opcao == 2:
            adicionar_usuario()
        if opcao == 3:
            opcao_submenu = submenu()
            if opcao_submenu == 1:
                buscar_livro()
            elif opcao_submenu == 2:
                buscar_artigo()
            elif opcao_submenu == 3:
                buscar_revista()
            elif opcao_submenu == 4:
                break
        if opcao == 4:
            buscar_usuario()
        if opcao == 5:
            emprestimo()
        if opcao == 6:
            devolucao()
        if opcao == 7:
            break

main()



def menu():
    print(f'\n Selecione uma das opções abaixo: ')

    while True:
        print(f'\n Opção 1: Adicionar material')
        print(f'\n Opção 2: Adicionar usuário')
        print(f'\n Opção 3: Buscar material')
        print(f'\n Opção 4: Buscar usuário')
        print(f'\n Opção 5: Realizar empréstimo')
        print(f'\n Opção 6: Devolução')
        print(f'\n Opção 7: Sair')

        opcao = input('\n')

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao > 0 and opcao < 8:
                return opcao
        print(f'\n Digite um valor válido')

def submenu():
    print(f'\n Selecione o tipo do material desejado: ')

    while True:
        print(f'\n Opção 1: Livro')
        print(f'\n Opção 2: Artigo')
        print(f'\n Opção 3: Revista')
        print(f'\n Opção 4: Voltar ao menu principal')

        opcao = input('\n')

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao > 0 and opcao < 5:
                return opcao
        print(f'\n Digite um valor válido')



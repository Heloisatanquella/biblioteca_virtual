codigo = 0

def novo_codigo():
    global codigo
    codigo = codigo + 1
    return codigo

def buscar(valor, lista, chave):
    for item in lista:
        if getattr(item, chave) == valor:
            return item
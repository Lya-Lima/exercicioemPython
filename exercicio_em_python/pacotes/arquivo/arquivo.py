dados = {}


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read().title())
        a.close()


def cadastrar(nome, n='desconhecido', i=0):
    try:
        a = open(nome, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{n:<30} {i:>3} anos \n')
        except:
            print('Erro ao fazer novo cadastro.')
        else:
            print('Cadastro feito com sucesso.')
            a.close()
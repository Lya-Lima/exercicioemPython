import menu
import arquivo

arquivo = 'arquivotexto.txt'
if not arquivo.arquivoexiste(arquivo):
    arquivo.criarArquivo(arquivo)
while True:
    resp = menu.menu_principal(['\033[33m1-\033[m \033[34mVer pessoas cadastradas\033[m',
                                '\033[33m2-\033[m \033[34mCadastrar nova pessoa\033[m',
                                '\033[33m3-\033[m \033[34mSair do sistema\033[m'])
    if resp == 1:
        #opção de listar o conteúdo do arquivo
        menu.linha()
        print('         Pessoas cadastradas            ')
        menu.linha()
        arquivo.lerArquivo(arquivo)
    elif resp == 2:
        #opção para cadastrar nova pessoa
        menu.linha()
        print('         Novo cadastro          ')
        menu.linha()
        while True:
            try:
                nome = str(input('Nome: '))
                idade = int(input('Idade: '))
            except (ValueError, TypeError):
                print('Você digitou valores inválidos. Tente novamente')
                continue
            else:
                arquivo.cadastrar(arquivo, nome, idade)
                break
    elif resp == 3:
        break

from time import sleep




def linha():
    print('-' * 40)


def menu_principal(lista):
    sleep(0.5)
    linha()
    print('          MENU PRINCIPAL          ')
    linha()
    for item in lista:
        print(item)
    linha()
    try:
        opc = int(input(f'\033[33mDigite sua opção:  \033[m '))
        if opc < 1 or opc > 3:
            print(f'\033[31mErro!\033[m Você digitou um valor inválido. Tente novamente.')
    except (ValueError, TypeError):
        print(f'\033[31mErro!\033[m Você digitou um valor inválido. Tente novamente.')
    except (KeyboardInterrupt):
        print(f'Entrada de dados interrompida pelo usuário. ')
    except Exception as erro:
        print('Infelizmente tivemos um problema...')
        print(f'Problema encontrado: {erro.__class__}')
    else:
        return opc

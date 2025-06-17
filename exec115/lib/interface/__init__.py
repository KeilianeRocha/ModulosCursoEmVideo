def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[0;31mEntrada de dados interompida pelo usuário! Digite um número inteiro válido!\033[m")
            return 0
        else:
            return n1

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc


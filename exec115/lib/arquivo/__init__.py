from exec115.lib.interface import *

def arquivoExiste(nome):
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
        print('\033[0;31mHouve um erro na criação do Arquivo!\033[m')
    else:
        print(f'\033[0;32mArquivo {nome} criado com Sucesso!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[0;31mErro ao criar o Arquivo!\033[m')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrarArquivo(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[0;31mErro na abertura do Arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[0;31mErro ao Cadastrar os Dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado com Sucesso!')
            a.close()




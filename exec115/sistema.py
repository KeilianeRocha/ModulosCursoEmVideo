from exec115.lib.interface import * # '*' importando tudo
from exec115.lib.arquivo import *
from  time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

#cabecalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['Ver Pessoa Cadastrada','Cacadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
        #cabecalho('1 - Ver Pessoa Cadastrada')
    elif resposta == 2:
        #cabecalho('2 - Cacadastrar Nova Pessoa')
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        #cpf = int(input('CPF: '))
        cadastrarArquivo(arq, nome, idade)
    elif resposta == 3:
        cabecalho('3 - Sair do Sistema... Até logo!')
        break
    else:
       print('\033[0;31mERRO! Digite uma opção válida\033[m')
    sleep(2)

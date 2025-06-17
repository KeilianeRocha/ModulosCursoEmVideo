from exec115.lib.interface import *
#cabecalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['Ver Pessoa Cadastrada','Cacadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        print('Ver Pessoa Cadastrada')
    elif resposta == 2:
        print('Cacadastrar Nova Pessoa')
    elif resposta == 3:
        print('Sair do Sistema')
        break
    else:
       print('ERRO! Digite uma opção válida')

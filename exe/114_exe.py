# TODO:
# Crie um código em Python que teste se o site https://www.pudim.com.br/ está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br/")
except urllib.error.URLError:
    print("O site Pudim não esta acessível no momento")
else:
    print("Site acessado com sucesso!")
    # print(site.read()) # ler o Html do site * opcional
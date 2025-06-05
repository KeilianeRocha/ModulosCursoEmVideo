# from moeda import aumentar, diminuir, dobro, metade, moeda # não é o recomendado
from exec110 import moeda  # recomendado

p = float(input("Digite o preço: R$ "))
moeda.resumo(p) # se não colocar os valores aqui, ele vai considerar os que estão no módulo 'moeda'

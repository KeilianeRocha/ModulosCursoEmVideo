# from moeda import aumentar, diminuir, dobro, metade, moeda # não é o recomendado
from exec111.utilidadescev import moeda

p = float(input("Digite o preço: R$ "))
moeda.resumo(p, 35, 22) # se não colocar os valores aqui, ele vai considerar os que estão no módulo 'moeda'

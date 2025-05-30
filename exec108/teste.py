# from moeda import aumentar, diminuir, dobro, metade, moeda # não é o recomendado
from exec108 import moeda  # recomendado

p = float(input("Digite o preço: R$ "))

print(
    f""" 
Aumentar 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p, 10))}
Diminuir 5% de {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, 5))}
O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}
A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}
"""
)

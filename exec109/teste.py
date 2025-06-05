# from moeda import aumentar, diminuir, dobro, metade, moeda # não é o recomendado
  # recomendado
from exec110 import moeda

p = float(input("Digite o preço: R$ "))

print(
    f""" 
Aumentar 10%, temos {moeda.aumentar(p, 10, True)}
Diminuir 5%, temos {moeda.diminuir(p, 5, True)}
O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}
A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}
"""
)

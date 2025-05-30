#from moeda import aumentar, diminuir, dobro, metade # não é o recomendado
from exec107 import moeda # recomendado

p = float(input("Digite o preço: R$ "))

print(f""" 
Aumentar 10% de R${p} é R${moeda.aumentar(p, 10)}
Diminuir 5% de R${p} temos R${moeda.diminuir(p, 5)}
O dobro de R${p} é R${moeda.dobro(p)}
A metade de R${p} é R${moeda.metade(p)}
""")
# MÓDULOS E PACOTES
Módulização → focos

💡 Ato de construir modulos (dividir para consquistar)

💡 Surgiu no início da décata de 60

💡 Sistemas ficando cada vez maiores

💡 Foco: dividir um programa grande

💡 Foco: aumentar a legibilidade

## Exemplo prático

[numeros.py](numeros.py) → código principal e funcoes

[uteis.py](uteis.py) → Modulação das funcoes do código
```Python
def fatoral(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


    num = int(input("Digite um número: "))
    fat = fatorial(num)
    print(f"O fatorial de {num} é {fat}")
```

Modulação → vantagens

💡 Organização do código

💡 Facilidade na manutenção

💡 Ocultação de código detalhado

💡 Reutilização de módulos em outros projetos (copiando o arquivo ´uteis´)

## PACOTES
Pastas que possuem módulos
![alt text](image.png)
![alt text](image-1.png)
A importação pode ser

→ import uteis ou → from uteis import datas
## Exemplo prático
```Python
def fatoral(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


    num = int(input("Digite um número: "))
    fat = fatorial(num)
    print(f"O fatorial de {num} é {fat}")
```

## 💡 Anotações
- Para o Python todo aquivo '.py' pode ser um módulo, deste que ele tenha 
funções internas
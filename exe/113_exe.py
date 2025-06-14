# TODO:
#  Rescreva a função leiaInt() do desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido.
# Criei também uma função leiaFloat()com a mesma funcionalidade

def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[0;31mEntrada de dados interompida pelo usuário! Digite um número inteiro válido!\033[m")
            return 0
        else:
            return n1


def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número real válido!\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[0;31mEntrada de dados interompida pelo usuário! Digite um número inteiro válido!\033[m")
            return 0
        else:
            return n2



# Programa principal
n1 = leiaInt("Digite um número: ")
n2 = leiaFloat("Digite um real: ")
print(f" O número inteiro digitado foi {n1} e o real foi {n2}")
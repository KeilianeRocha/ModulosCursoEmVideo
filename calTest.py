try: # tenta
    a = int(input("Numerador: ")) # Se a = 2
    b = int(input("Denominador:" )) # Se b = 0
    r = a/b # Gera erro, não se devide por '0'
#except: # se der problema
#print("Infelizmente tivemos um problema (。_。)") # ZeroDivisionError: Mantem so aminha mensagem de erro
#except Exception as erro: # se der problema, mas quero ver o motivo
    #print(f" O problema encontrado foi {erro.__class__}")
except Exception: # se der problema, mas quero ver o motivo
    print("Não é possível dividir um número por zero")
except (ValueError, TypeError):
    print("Tivemos um problema com o tipo de dado que você digitou")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados")
except Exception as erro:
    print(f"O erro foi {erro.__cause__}")
else: # Não deu problema
    print(f"O resultado é {r:.1f}")
finally: # Vai acontecer independente se deu erro ou não (finally/else é opcional)
    print("Obrigada! Volte sempre!")

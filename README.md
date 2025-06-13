# Trataento de erros

- erro sintaxe 
  - primt("oi")
 
- erro semantico
   - print(x) → não iniciei a variavel 'x' → NameError
- Excessão 
  - quando o erro não é de sintaxe ele se chama erro
     - n = int(input('Numero: ')) → a variavel 'n'é do tipo 'int'
    print("Você digitou {n}) → como retorno ele espera um tipo 'int', 
    mas eu escrevi um tipo 'str' → ValueError
     - a = int(input("Numerador: ")) # Se a = 2
     - b = int(imput("Denominador:" )) # Se b = 0
    r = a/b # Gera erro, pois na divisão não se devide por '0'
    print(f"O resultado é {r}") → ZerroDivisonError
     - outros Exemplos
     - n = 2/'2' # Python não divide int com str → TypeError
     - lst = [3,6,4] # o indice começa com 0, então ela retorna ate o 2 → IndexError
     - Durante a importação não importar o modulo → ModuleNotFoundError
  - Toda exceção é filha de uma classe maior Exception
## Como tratar?
- comando 
````python
try: 
    operacao
except:
    falhou
````
Todo 'try' pode ter mais de uma 'Exception' mas sempre criando seus proprios blocos
````python
try: 
    operacao
except:
    falhou
except:
    falhou outra vez
````


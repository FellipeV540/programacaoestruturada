"""
casos try/except
-Uso quando não souber qual exceção pode subir
-OU quando não souber qual exceção pode subir
"""




"""
print("olá, mundo")  #funcionando.😊

print("olá, mundo"  #erro de sintaxe

x = 2
if x == 3
    print("erro")  #erro de sintaxe

numero = 'a'

if not numero.isnumeric():  #.Isnumeric checar se é numero e retorna True ou False
    print("numer")
"""

def divisao(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Erro! Impossível dividir por 0")
    except TypeError:
        print("Erro! cálculo não funcionou")

divisao('abc', 2)

def terceira_letra():
    try:
        nome = input("Informe seu nome: ")
        print(f"A terceira letra do seu nome é {nome[2]}")
        ret = nome[2]
    except Exception as err:
        print(f"Erro desconhecido, Erro: {err}")
        print(type(err))
        ret = "erro!"
    else:
        print("Leitura dos dados bem sucedida")
    finally:
        print("fim da função.")
        return ret

# divisao(0 , 0)
#print(terceira_letra())

class TamanhoExcedidoError(Exception):
    pass

def exibe_num(numero):
    if numero > 10:
        raise TamanhoExcedidoError

    print(numero)

exibe_num(15)

def func1():
    raise NotImplementedError

def func2():
    raise NotImplementedError

func1()
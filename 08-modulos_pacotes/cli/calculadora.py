"""
INterface por linha de comando (cli)
Calcuadora

Apresenta as opções da calculadora, e as operações disponiveis
Chama as operações de cálculo, conforme a seleção do usuário
"""
from numeros import decisor

def exibe_mensagem():
    print("""Bem-vindo à calculadora!
Insira um numero e pressione ENTER, em seguida digite uma operação (+, -, *, /),
depois outro numero enter bla bla bla""")

def iniciar():
    exibe_mensagem()
    n1 = float(input())
    operacao = input()
    n2 = float(input())
    print(n1, operacao, n2, "=", decisor.chama_calculadora(n1, n2, operacao))

iniciar()
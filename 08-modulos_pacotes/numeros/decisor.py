"""
Seleciona qual operação será realizada
"""
from numeros.operacoes import arit
from .operacoes import exp

def chama_calculadora(n1, n2, operacao):
    match operacao:
        case "+":
            return arit.soma(n1, n2)
        case "-":
            return arit.subtracao(n1, n2)
        case "*":
            return arit.multiplicacao(n1, n2)
        case "/":
            return arit.divisao(n1, n2)
        case "**":
            return exp.potencia(n1, n2)
        case "^":
            return exp.raiz(n1, n2)
        case _:
            return "erro, operação inválida"
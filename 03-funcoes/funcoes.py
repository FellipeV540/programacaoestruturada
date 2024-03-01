# funções

def traco(sep, tamanho)
    print(sep * tamanho)

# declarando/definindo funçoes
def cabecalho(titulo, sep= "-", tamanho= 30): #p1 parametro
    print(sep * tamanho)
    print(titulo)
    print(sep * tamanho)

# chamar função
cabecalho("RELATORIO DE FINANÇAS") #define parametro dentro do parenteses
cabecalho("RELATORIO DE CONTRATAÇÕES", 25, "=") #define parametro dentro do parenteses

# nao colocoar os parenteses significa que estou falando da funçao, e nao chamando
print(cabecalho)
print(cabecalho("ola", 25))



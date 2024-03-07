# exercício 2

# calcula delta
def cal_delta(a, b, c):
    return b**2 - 4 * a * c

# calcula as raizes
def cal_raizes(a, b, c):
    delta = cal_delta(a, b, c)
    if delta == 0:
        return [-b / (2 * a)]
    elif delta > 0:
        return [(-b + delta ** 0.5) / (2 * a), (-b - delta ** 0.5) / (2 * a)]
    else:
        return []

# pede os coeficientes
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

# printar as raizes
raizes = cal_raizes(a, b, c)

print("a primeira raiz é", raizes[0])
print("a segunda raiz é", raizes[1])

# exercício 2

# pede o ano para o usuário
ano = int(input("Informe o Ano: "))

# verifica se o ano é bissexto
bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

# print se o ano é bissexto
print(bissexto)

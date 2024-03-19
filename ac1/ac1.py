# exercício 1

# Pede os coeficientes
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

# Calcula delta
def cal_delta(a, b, c):
    return b**2 - 4 * a * c

# Calcula as raizes
def cal_raizes(a, b, c):
    delta = cal_delta(a, b, c)
    if delta == 0:
        return [-b / (2 * a)]
    elif delta > 0:
        return [(-b + delta ** 0.5) / (2 * a), (-b - delta ** 0.5) / (2 * a)]
    else:
        return "Essa raiz não é real"

# Exibir as raizes
raizes = cal_raizes(a, b, c)

print("a primeira raiz é", raizes[0])
print("a segunda raiz é", raizes[1])

# exercício 2

# Ler o ano fornecido pelo usuário
ano = int(input("Informe o ano: "))

# Verificar se o ano é bissexto
bissexto = (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)

# Exibir o resultado
if bissexto:
    print("True")
else:
    print("False")

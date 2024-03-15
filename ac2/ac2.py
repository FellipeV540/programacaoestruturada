def eq_seg_grau(a, b, c):
    delta = b**2 - 4 * a * c
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print("primeira raiz:", x1, "segunda raiz:", x2)

eq_seg_grau(2, 4, -6)

def bissexto(ano):
    bissexto_ano = (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)
    bissexto_ano = bool(bissexto_ano)
    print(bissexto_ano)

bissexto(1996)

def calcula_salario(valor_hora, num_horas):
    irpf = 0.275
    sal_liq = valor_hora * num_horas
    sal_liq = sal_liq * irpf
    print(sal_liq)

calcula_salario(50, 160)
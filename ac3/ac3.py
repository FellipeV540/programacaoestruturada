def determina_tipo_triangulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b and b == c:
            return "Equilátero"
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            return "Isósceles"
        elif (a != b and b != c):
            return "Escaleno"
    else:
        return "Não é triangulo"

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

testa_triangulo()

def dia_semana(dia):
    if 0 < dia < 8:
        if dia == 1:
            return "Domingo"
        elif dia == 2:
            return "Segunda-Feira"
        elif dia == 3:
            return "Terça-Feira"
        elif dia == 4:
            return "Quarta-Feira"
        elif dia == 5:
            return "Quinta-Feira"
        elif dia == 6:
            return "Sexta-Feira"
        elif dia == 7:
            return "Sábado"
    else:
        return "String Vazia"

def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

testa_dia_semana()

def calc():
    a = float(input("Primeiro Número: "))
    b = float(input("Segundo Número: "))
    op = (str(input("Operação Desejada: ")))

    if op.lower() == "soma":
        print(a + b)
    elif op.lower() == "subtracao":
        print(a - b)
    elif op.lower() == "multiplicacao":
        print(a * b)
    elif op.lower() == "divisao":
        print(a / b)
    else:
        print("Operação Inválida")

calc()

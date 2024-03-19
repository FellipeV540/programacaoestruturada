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